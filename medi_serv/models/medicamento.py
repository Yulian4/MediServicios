from odoo import models, fields

class Medicamento (models.Model):
    _name = "medi_serv.medicamento"
    _description  = "Tabla de medicamentos"


    codigo = fields.Integer (string="Codigo" ,required = True)
    nombre = fields.Char (string="Nombre", required=True)
    principio_activo = fields.Char(string="Principio Activo")
    forma_farmaceutica = fields.Selection([
        ('tableta', 'Tableta'),
        ('jarabe', 'Jarabe'),
        ('inyectable', 'Inyectable'),
        ('capsula', 'Cápsula'),
        ('unguento', 'Ungüento'),
    ], string="Forma Farmacéutica")
    concentracion = fields.Char(string="Concentración")
    fecha_vencimiento = fields.Date(string="Fecha de Vencimiento")
    via_administracion = fields.Selection([
        ('oral', 'Oral'),
        ('intravenosa', 'Intravenosa'),
        ('intramuscular', 'Intramuscular'),
        ('topica', 'Tópica'),
    ], string="Vía de Administración")
    dosis_recomendada = fields.Char(string="Dosis Recomendada")