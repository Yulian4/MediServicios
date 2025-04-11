from odoo import http
from odoo.http import request

class PacienteController(http.Controller):

    @http.route('/pacientes', type='http', auth="public", website=True)
    def lista_pacientes(self, **kw):
        pacientes = request.env['medi_serv.paciente'].sudo().search([])
        return request.render('medi_serv.template_pacientes', {
            'pacientes': pacientes
        })

    @http.route('/paciente/crear', auth='public', website=True, type='http', methods=['GET', 'POST'])
    def create_paciente(self, **post):
        if request.httprequest.method == 'POST':
            paciente_data = {
                'name': post.get('name'),
                'apellidos': post.get('apellidos'),
                'fecha_nacimiento': post.get('fecha_nacimiento'),
                'tipodoic': post.get('tipodoic'),
                'telefono': post.get('telefono'),
                'email': post.get('email'),
                'direccion': post.get('direccion'),
                'sexo': post.get('sexo'),
                'acompanante': post.get('acompanante') == 'si',
                'nombre_acompanante': post.get('nombre_acompanante'),
                'telefono_acompanante': post.get('telefono_acompanante'),
                'parentezco_acompanante': post.get('parentezco_acompanante'),
            }

            # Validación básica por si acaso
            if not paciente_data['name']:
                return "Error: El campo Nombre es obligatorio."

            # Crear el paciente
            request.env['medi_serv.paciente'].sudo().create(paciente_data)
            return request.redirect('/pacientes')

        # Renderizar el formulario en caso de método GET
        return request.render('medi_serv.paciente_form_template')
    
    @http.route('/paciente/editar/<int:paciente_id>', type='http', auth='public', website=True)
    def editar_paciente(self, paciente_id, **kw):
        paciente = request.env['medi_serv.paciente'].sudo().browse(paciente_id)
        return request.render('tu_modulo.template_editar_paciente', {'paciente': paciente})

    @http.route('/paciente/editar/<int:paciente_id>', type='http', auth='public', website=True, methods=['POST'])
    def actualizar_paciente(self, paciente_id, **post):
        paciente = request.env['medi_serv.paciente'].sudo().browse(paciente_id)
        paciente.write({
            'name': post.get('name'),
            'apellidos': post.get('apellidos'),
            'fecha_nacimiento': post.get('fecha_nacimiento'),
            'telefono': post.get('telefono'),
            'email': post.get('email'),
            'direccion': post.get('direccion'),
        })
        return request.redirect('/pacientes')