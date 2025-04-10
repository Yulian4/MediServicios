from odoo import models, fields, api

class Paciente(models.Model):
    _name = 'medi_serv.paciente'
    _description = 'Paciente'

    name = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    tipodoic = fields.Selection([('ti', 'TI'), ('cc', 'CC'),], string='Tipo de Documento')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    sexo = fields.Selection([
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
    ], string='Sexo')
    acompanante = fields.Selection([ ('si', 'Sí'),
            ('no', 'No'),],
        string='Acompañante')
    
    
    