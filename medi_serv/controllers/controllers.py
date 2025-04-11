from odoo import http
from odoo.http import request


class PaginaInicioController(http.Controller):

    @http.route('/inicio', type='http', auth="public", website=True)
    def inicio(self, **kw):
        # Esto renderiza la plantilla de inicio que creaste
        return request.render('medi_serv.inicio_template')
    
    
    
class FacturaController(http.Controller):

    @http.route('/facturas', auth='public', website=True)
    def mostrar_facturas(self, **kw):
        # Obtener todas las facturas
        facturas = request.env['medi_serv.factura'].sudo().search([])
        
        # Renderizar la plantilla con las facturas obtenidas
        return request.render('medi_serv.template_facturas', {
            'facturas': facturas
        })
        

    @http.route('/paciente/crear', auth='public', website=True, type='http', methods=['GET', 'POST'])
    def create_paciente(self, **kwargs):
        if request.httprequest.method == 'POST':
            # Recoger los datos enviados desde el formulario
            paciente_data = {
                'name': kwargs.get('name'),
                'apellidos': kwargs.get('apellidos'),
                'fecha_nacimiento': kwargs.get('fecha_nacimiento'),
                'telefono': kwargs.get('telefono'),
                'email': kwargs.get('email'),
                'sexo': kwargs.get('sexo'),
                'acompanante': kwargs.get('acompanante'),
                'nombre_acompanante': kwargs.get('nombre_acompanante'),
                'telefono_acompanante': kwargs.get('telefono_acompanante'),
                'parentezco_acompanante': kwargs.get('parentezco_acompanante'),
            }
            
            # Crear el paciente
            request.env['medi_serv.paciente'].sudo().create(paciente_data)
            
            # Redirigir al listado de pacientes
            return request.redirect('/pacientes')

        # Si la solicitud es GET, mostrar el formulario vacío
        paciente = request.env['medi_serv.paciente'].sudo().new({})
        return request.render('medi_serv.paciente_create', {
            'form': paciente
        })
        
    @http.route('/paciente/editar/<int:paciente_id>', auth='public', website=True)
    def editar_paciente_form(self, paciente_id, **kw):
        paciente = request.env['medi_serv.paciente'].sudo().browse(paciente_id)
        return request.render('medi_serv.paciente_edit', {
            'paciente': paciente
        })


    @http.route('/paciente/editar/todo', auth='public', website=True, methods=['POST'])
    def editar_paciente_guardar(self, **post):
        paciente_id = int(post.get('id'))
        paciente = request.env['medi_serv.paciente'].sudo().browse(paciente_id)
        if paciente.exists():
            paciente.sudo().write({
                'name': post.get('name'),
                'apellidos': post.get('apellidos'),
                'fecha_nacimiento': post.get('fecha_nacimiento'),
                'telefono': post.get('telefono'),
                'email': post.get('email'),
                'sexo': post.get('sexo'),
                'acompanante': post.get('acompanante'),
                'nombre_acompanante': post.get('nombre_acompanante'),
                'telefono_acompanante': post.get('telefono_acompanante'),
                'parentezco_acompanante': post.get('parentezco_acompanante'),
            })
        return request.redirect('/pacientes')

