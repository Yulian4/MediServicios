from odoo import models, fields

class Habitacion(models.Model):
    _name = 'medi_serv.habitacion'
    _description = 'Gestión de Habitaciones'

    nombre = fields.Char(string='Nombre', required=True)
    codigo = fields.Char(string='Código', required=True)
    disponible = fields.Boolean(string='Disponible', default=True)
