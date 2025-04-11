from odoo import models, fields

class RecuperacionHosp(models.Model):
    _name = 'medi_serv.recuperacion_hosp'
    _description = 'Recuperación Hospitalaria'

    paciente_id = fields.Many2one('medi_serv.paciente', string='Paciente', required=True)
    fecha_ingreso = fields.Date(string='Fecha de Ingreso', required=True)
    fecha_egreso = fields.Date(string='Fecha de Egreso')
    estado_paciente = fields.Selection([
        ('estable', 'Estable'),
        ('crítico', 'Crítico'),
        ('observación', 'En Observación')
    ], string='Estado del Paciente')
    cuidados = fields.Text(string='Cuidados Especiales')

    evolucion_ids = fields.One2many('medi_serv.evolucion_clinica', 'recuperacion_id', string='Evoluciones Clínicas')
    enfermeria_ids = fields.One2many('medi_serv.nota_enfermeria', 'recuperacion_id', string='Notas de Enfermería')
    visita_ids = fields.One2many('medi_serv.visita_medica', 'recuperacion_id', string='Visitas Médicas')

class EvolucionClinica(models.Model):
    _name = 'medi_serv.evolucion_clinica'
    _description = 'Evolución Clínica'

    recuperacion_id = fields.Many2one('medi_serv.recuperacion_hosp', string='Recuperación', ondelete='cascade')
    fecha = fields.Datetime(string='Fecha', default=fields.Datetime.now, required=True)
    descripcion = fields.Text(string='Descripción', required=True)
    medico_id = fields.Many2one('medi_serv.medico', string='Médico Responsable')

class NotaEnfermeria(models.Model):
    _name = 'medi_serv.nota_enfermeria'
    _description = 'Nota de Enfermería'

    recuperacion_id = fields.Many2one('medi_serv.recuperacion_hosp', string='Recuperación', ondelete='cascade')
    fecha = fields.Datetime(string='Fecha', default=fields.Datetime.now, required=True)
    nota = fields.Text(string='Nota', required=True)
    enfermero_id = fields.Many2one('medi_serv.medico', string='Enfermero/a')

class VisitaMedica(models.Model):
    _name = 'medi_serv.visita_medica'
    _description = 'Visita Médica'

    recuperacion_id = fields.Many2one('medi_serv.recuperacion_hosp', string='Recuperación', ondelete='cascade')
    fecha = fields.Datetime(string='Fecha de Visita', default=fields.Datetime.now, required=True)
    motivo = fields.Text(string='Motivo de la Visita')
    medico_id = fields.Many2one('medi_serv.medico', string='Médico Visitante')

    