from odoo import fields, models, api

class Factura(models.Model):
    _name = 'medi_serv.factura'
    _description = 'Factura'

    name = fields.Char(string='Número de Factura', required=True, copy=False, readonly=True, index=True, default=lambda self: ('Nuevo'))
    paciente_id = fields.Many2one('medi_serv.paciente', string='Paciente', required=True)
    fecha_factura = fields.Date(string='Fecha de Factura', default=fields.Date.context_today, required=True)
    total_medicamentos = fields.Float(string='Total', compute='_compute_total', store=True)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
    ], string='Estado', default='pendiente')

    @api.depends('paciente_id')
    def _compute_total(self):
        for record in self:
            # Buscar todas las preparaciones quirúrgicas del paciente
            preparaciones = self.env['medi_serv.preparacion_q'].search([('paciente_id', '=', record.paciente_id.id)])
            # Sumar los precios de los medicamentos asociados
            total = sum(preparacion.medicamento_id.precio for preparacion in preparaciones)
            record.total_medicamentos = total