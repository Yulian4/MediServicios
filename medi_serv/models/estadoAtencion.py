from odoo import models, fields, api

class Estado(models.Model):
    _name = 'medi_serv.estado'
    _description = 'Registro de Estado Médico'

    paciente = fields.Char(string='Paciente', required=True)
    presion_sistolica = fields.Integer(string='Presión Sistólica', default=0)
    presion_diastolica = fields.Integer(string='Presión Diastólica', default=0)
    temperatura = fields.Float(string='Temperatura', default=36.5)
    frecuencia_cardiaca = fields.Integer(string='Frecuencia Cardíaca', default=70)

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

    kanban_color = fields.Integer(compute='_compute_kanban_color', store=True)

    @api.depends('presion_sistolica', 'presion_diastolica', 'temperatura', 'frecuencia_cardiaca')
    def _calcular_tipo_atencion(self):
        for record in self:
            if record.temperatura >= 39 or record.frecuencia_cardiaca >= 120:
                record.tipo_atencion = 'urgencia'
            elif record.presion_sistolica >= 140 or record.presion_diastolica >= 90:
                record.tipo_atencion = 'cirugia'
            else:
                record.tipo_atencion = 'consulta'

    @api.depends('tipo_atencion')
    def _compute_kanban_color(self):
        for record in self:
            if record.tipo_atencion == 'urgencia':
                record.kanban_color = 1  # Rojo
            elif record.tipo_atencion == 'cirugia':
                record.kanban_color = 2  # Azul
            elif record.tipo_atencion == 'consulta':
                record.kanban_color = 10  # Verde
            else:
                record.kanban_color = 0
