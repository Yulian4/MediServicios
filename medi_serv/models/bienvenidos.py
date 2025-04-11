from odoo import models, fields

class Bienvenida(models.Model):
    _name = 'medi_serv.bienvenida'
    _description = 'Pantalla de Bienvenida'

    name = fields.Char(string='Mensaje', default='Bienvenidos a MediServicios')