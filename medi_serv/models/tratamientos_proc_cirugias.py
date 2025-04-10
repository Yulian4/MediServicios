from odoo import models, fields, api

class TratamientosProcCirugias(models.Model):
    _name = 'medi_serv.trata_proc_cirugia'
    _description = 'Tratamientos y Procedimientos Quirúrgicos'

    codigo = fields.Char(string='Código', required=True)
    name = fields.Char(string='Nombre del Tratamiento/Procedimiento', required=True)
    descripcion = fields.Text(string='Descripción')
    costo = fields.Float(string='Costo', required=True)
    