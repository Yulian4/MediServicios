from odoo import fields, models

class Insumo (models.Model):
    _name = "medi_serv.insumo"
    _description="Tabla de insumos"

    nombre = fields.Char(string="Nombre", required=True)
    tipo = fields.Selection([
        ('descartable', 'Descartable'),
        ('reutilizable', 'Reutilizable'),
        ('otros', 'Otros'),
    ], string="Tipo de Insumo", required=True)
    descripcion = fields.Text(string="Descripción")
    unidad_medida = fields.Selection([
        ('unidad', 'Unidad'),
        ('caja', 'Caja'),
        ('paquete', 'Paquete'),
        ('bolsa', 'Bolsa'),
    ], string="Unidad de Medida")
    stock = fields.Integer(string="Stock Disponible")
    precio_unitario = fields.Float(string="Precio Unitario")
    fecha_vencimiento = fields.Date(string="Fecha de Vencimiento")
    