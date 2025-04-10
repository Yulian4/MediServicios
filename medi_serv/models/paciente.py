from odoo import models, fields, api

class Paciente(models.Model):
    _name = 'medi_serv.paciente'
    _description = 'Paciente'

    name = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    edad = fields.Integer(string='Edad',compute="compute_edad", required=True)
    tipodoic = fields.Selection([('ti', 'TI'), ('cc', 'CC'),], string='Tipo de Documento')
    
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    direccion = fields.Char(string='Dirección')
    sexo = fields.Selection([
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
    ], string='Sexo')
    acompanante = fields.Selection([ ('si', 'Sí'),
            ('no', 'No'),],
        string='Acompañante')
    nombre_acompanante = fields.Char(string='Nombre del Acompañante')
    telefono_acompanante = fields.Char(string='Teléfono del Acompañante')
    parentezco_acompanante = fields.Char(string='Parentesco del Acompañante')
    
    @api.depends('fecha_nacimiento')
        
    def compute_edad(self):
        for record in self:
            if record.fecha_nacimiento:
                edad = fields.Date.today().year - record.fecha_nacimiento.year
                record.edad = edad if edad >= 0 else 0
            else:
                record.edad = 0