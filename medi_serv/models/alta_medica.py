from odoo import models, fields, api

class AltaMedica(models.Model):
    _name = 'medi_serv.alta_medica'
    _description = 'Alta Médica'

    paciente_id = fields.Many2one('medi_serv.paciente', string='Paciente', required=True)
    fecha_alta = fields.Date(string='Fecha de Alta', required=True)
    motivo_alta = fields.Selection([
        ('recuperacion', 'Recuperación'),
        ('traslado', 'Traslado'),
        ('voluntaria', 'Alta Voluntaria'),
        ('fallecimiento', 'Fallecimiento')
    ], string='Motivo del Alta')
    recomendaciones = fields.Text(string='Recomendaciones al Paciente')
