from odoo import fields, models, api

class PreparacionQ(models.Model):
    _name = 'medi_serv.preparacion_q'
    _description = 'PreparacionQ'

    paciente_id = fields.Many2one('medi_serv.paciente', string='Paciente', required=True)
    descripcion = fields.Text(string='Descripción')
    fecha_preparacion = fields.Date(string='Fecha de Preparación', default=fields.Date.context_today, required=True)
    medicamento_id = fields.Many2one('medi_serv.medicamento', string='Medicamento', required=True)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('completado', 'Completado'),
    ], string='Estado', default='pendiente')
    