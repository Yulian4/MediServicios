from odoo import fields, models, api

class Factura(models.Model):
    _name = 'medi_serv.factura'
    _description = 'Factura'

    name = fields.Char(string='Número de Factura', required=True, copy=False, readonly=True, index=True, default=lambda self: ('Nuevo'))
    paciente_id = fields.Many2one('medi_serv.paciente', string='Paciente', required=True)
    fecha_factura = fields.Date(string='Fecha de Factura', default=fields.Date.context_today, required=True)

    total_medicamentos = fields.Float(string='Total Medicamentos', compute='_compute_total', store=True)
    total_tratamientos = fields.Float(string='Total Tratamientos', compute='_compute_total', store=True)
    total_general = fields.Float(string='Total Factura', compute='_compute_total', store=True)

    #total_medicamentos = fields.Float(string='Total', compute='_compute_total', store=True)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
    ], string='Estado', default='pendiente')

    @api.depends('paciente_id')
    def _compute_total(self):
        for record in self:
            # Buscar todas las preparaciones quirúrgicas del paciente
            preparaciones = self.env['medi_serv.preparacion_q'].search([
                ('paciente_id', '=', record.paciente_id.id)
            ])

            total_meds = 0.0
            total_trats = 0.0

            for prep in preparaciones:
                # Sumar totales de medicamentos
                for linea_med in prep.medicamento_line_ids:
                    if linea_med.medicamento_id:
                        total_meds += (linea_med.cantidad or 0.0) * (linea_med.medicamento_id.precio or 0.0)

                # Sumar totales de tratamientos
                for linea_trat in prep.tratamiento_line_ids:
                    if linea_trat.tratamiento_id:
                        total_trats += (linea_trat.cantidad or 0.0) * (linea_trat.tratamiento_id.costo or 0.0)

            record.total_medicamentos = total_meds
            record.total_tratamientos = total_trats
            record.total_general = total_meds + total_trats
    # def _compute_total(self):
    #     for record in self:
    #         # Buscar todas las preparaciones quirúrgicas del paciente
    #         preparaciones = self.env['medi_serv.preparacion_q'].search([('paciente_id', '=', record.paciente_id.id)])
    #         # Sumar los precios de los medicamentos asociados
    #         total = sum(preparacion.medicamento_id.precio for preparacion in preparaciones)
    #         record.total_medicamentos = total
            
    def imprimir_factura(self):
        return self.env.ref('medi_serv.report_factura').report_action(self)