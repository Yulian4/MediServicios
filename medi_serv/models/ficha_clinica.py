from odoo import models, fields, api, exceptions

class FichaClinica(models.Model):
    _name = 'medi_serv.ficha_clinica'
    _description = 'Ficha Clinica'
    _rec_name = 'paciente_id'

    
    paciente_id = fields.Many2one('medi_serv.paciente', string='Paciente', required=True, readonly=True)
    
#     historia_ids = fields.One2many('medi_serv.historia_clinica', 'id_pac', string='Historias Clínicas', readonly=True)
#     preparacion_ids = fields.One2many('medi_serv.preparacion_q', 'paciente_id', string='Preparaciones Quirúrgicas', readonly=True)
    
    # Campos relacionados a desarrollar en el futuro
    # registro_cirugia_ids = fields.One2many('medi_serv.registro_cirugia', 'paciente_id', string='Registros de Cirugía', readonly=True)
    # recuperacion_ids = fields.One2many('medi_serv.recuperacion_hosp', 'paciente_id', string='Recuperaciones', readonly=True)
    # alta_medica_ids = fields.One2many('medi_serv.alta_medica', 'paciente_id', string='Altas Médicas', readonly=True)