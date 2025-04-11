from odoo import models, fields, api

class RegistroCirugia(models.Model):
    _name = 'medi_serv.registro_cirugia'
    _description = 'Registro de Cirugía'

    paciente_id = fields.Many2one('medi_serv.paciente', string='Paciente', required=True)
    fecha_cirugia = fields.Date(string='Fecha de Cirugía', required=True)
    tipo_cirugia = fields.Char(string='Tipo de Cirugía')
    medico_responsable = fields.Char(string='Médico Responsable')
    observaciones = fields.Text(string='Observaciones')
    