from odoo import fields, models, api

class PreparacionQ(models.Model):
    _name = 'medi_serv.preparacion_q'
    _description = 'PreparacionQ'
    _rec_name = 'name'

    paciente_id = fields.Many2one('medi_serv.paciente', string='Paciente', required=True)
    descripcion = fields.Text(string='Descripción')
    fecha_preparacion = fields.Date(string='Fecha de Preparación', default=fields.Date.context_today, required=True)
    
    medicamento_line_ids = fields.One2many('medi_serv.preparacionq_medicamento', 'preparacion_id', string='Medicamentos')
    tratamiento_line_ids = fields.One2many('medi_serv.preparacionq_tratamiento', 'preparacion_id', string='Tratamientos')
    
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('completado', 'Completado'),
    ], string='Estado', default='pendiente')

class PreparacionQMedicamentoLine(models.Model):
    _name = 'medi_serv.preparacionq_medicamento'
    _description = 'Medicamentos en Preparación Quirúrgica'

    preparacion_id = fields.Many2one('medi_serv.preparacion_q', string='Preparación', required=True, ondelete='cascade')
    medicamento_id = fields.Many2one('medi_serv.medicamento', string='Medicamento', required=True)
    cantidad = fields.Integer(string='Cantidad', required=True)

class PreparacionQTratamientoLine(models.Model):
    _name = 'medi_serv.preparacionq_tratamiento'
    _description = 'Tratamientos en Preparación Quirúrgica'

    preparacion_id = fields.Many2one('medi_serv.preparacion_q', string='Preparación', required=True, ondelete='cascade')
    tratamiento_id = fields.Many2one('medi_serv.trata_proc_cirugia', string='Tratamiento', required=True)
    cantidad = fields.Integer(string='Cantidad', required=True)