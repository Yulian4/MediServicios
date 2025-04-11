from odoo import http
from odoo.http import request

class FacturaController(http.Controller):

    @http.route('/facturas', auth='public', website=True)
    def mostrar_facturas(self, **kw):
        # Obtener todas las facturas
        facturas = request.env['medi_serv.factura'].sudo().search([])
        
        # Renderizar la plantilla con las facturas obtenidas
        return request.render('medi_serv.template_facturas', {
            'facturas': facturas
        })
        


    @http.route('/factura/crear', auth='public', website=True, type='http', methods=['GET', 'POST'], csrf=False)
    def create_factura(self, **kwargs):
        if request.httprequest.method == 'POST':
            factura_data = {
                'paciente_id': int(kwargs.get('paciente_id')),
                'fecha_factura': kwargs.get('fecha_factura'),
                # 'name' se autogenera si lo dejas como 'Nuevo'
            }
            request.env['medi_serv.factura'].sudo().create(factura_data)
            return request.redirect('/facturas')

        # Datos vacíos para el formulario
        factura_data = {
            'fecha_factura': '',
        }

        pacientes = request.env['medi_serv.paciente'].sudo().search([])
        return request.render('medi_serv.facturaCreate', {
            'factura_data': factura_data,
            'pacientes': pacientes
        })
        
    @http.route('/factura/<int:factura_id>', type='http', auth='public', website=True)
    def ver_factura(self, factura_id):
        factura = request.env['medi_serv.factura'].sudo().browse(factura_id)
        if not factura.exists():
            return request.not_found()

        return request.render('medi_serv.vista_factura_detalle', {
            'factura': factura
        })
    
    #implementacion de api para medicamentos
    class MedicamentoController(http.Controller):

        @http.route('/medicamentos', auth='public', website=True)
        def mostrar_medicamentos(self, **kw):
            medicamentos = request.env['medi_serv.medicamento'].sudo().search([])
            return request.render('medi_serv.vista_medicamento_web', {
                'medicamentos': medicamentos
            })

    @http.route('/lobby/admin', auth='public', website=True)
    def lobby(self, **kwargs):
        return request.render('medi_serv.lobby_template', {})
