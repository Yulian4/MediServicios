from odoo import models, fields, api

class RegistroCirugia(models.Model):
    _name = 'medi_serv.registro_cirugia'
    _description = 'Registro de Cirugía'

    paciente_id = fields.Many2one('medi_serv.paciente', string='Paciente', required=True)
    fecha_cirugia = fields.Date(string='Fecha de Cirugía', required=True)
    medico_responsable_id = fields.Many2one('medi_serv.medico', string='Médico Responsable', help='Médico encargado de la cirugía')
    descripcion = fields.Text(string='Descripcion')