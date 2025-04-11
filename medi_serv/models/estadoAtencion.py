from odoo import models, fields, api

class Estado(models.Model):
    _name = 'medi_serv.estado'
    _description = 'Registro de Estado Médico'

    paciente = fields.Char(string='Paciente', required=True)
    presion = fields.Char(string='Presión Arterial')
    temperatura = fields.Float(string='Temperatura')
    frecuencia_cardiaca = fields.Integer(string='Frecuencia Cardíaca')
    tipo_atencion = fields.Selection([
        ('consulta', 'Consulta'),
        ('cirugia', 'Cirugía'),
        ('urgencia', 'Urgencia')
    ], string='Tipo de Atención', compute='_calcular_tipo_atencion', store=True)
    estado = fields.Selection([
        ('esperando', 'Esperando'),
        ('en_proceso', 'En Proceso'),
        ('atendido', 'Atendido')
    ], string='Estado', default='esperando')

    @api.depends('presion', 'temperatura', 'frecuencia_cardiaca')
    def _calcular_tipo_atencion(self):
        for record in self:
            if record.temperatura >= 39 or record.frecuencia_cardiaca >= 120:
                record.tipo_atencion = 'urgencia'
            elif record.presion and ('140' in record.presion or '90' in record.presion):
                record.tipo_atencion = 'cirugia'
            else:
                record.tipo_atencion = 'consulta'
