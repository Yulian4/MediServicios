from odoo import models, fields, api

class Medico(models.Model):
    _name = 'medi_serv.medico'
    _description = 'Medico'

    name = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    especialidad = fields.Selection([('medicina_general', 'Medicina General'),
                                        ('medico_urg', 'Medico Urgencias'),
                                        ], string='Especialidad')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    _sql_constraints = [
        ('unique_email', 'UNIQUE(email)', 'Este correo ya está registrado. Debe ser único.'),
    ]
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    sexo = fields.Selection([
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
    ], string='Sexo')
    sede = fields.Char( string='Sede',required=True)
    
    