from odoo import http
from odoo.http import request

class MedicoController(http.Controller):

    @http.route('/medicos', type='http', auth='public', website=True)
    def listar_medicos(self, **kw):
        medicos = request.env['medi_serv.medico'].sudo().search([])
        return request.render('medi_serv.lista_medicos', {'medicos': medicos})

    @http.route('/medico/crear', type='http', auth='public', website=True)
    def crear_medico_form(self, **kw):
        return request.render('medi_serv.crear_medico', {})

    @http.route('/medico/guardar', type='http', auth='public', website=True, csrf=False)
    def guardar_medico(self, **post):
        request.env['medi_serv.medico'].sudo().create({
            'name': post.get('name'),
            'apellidos': post.get('apellidos'),
            'especialidad': post.get('especialidad'),
            'telefono': post.get('telefono'),
            'email': post.get('email'),
            'fecha_nacimiento': post.get('fecha_nacimiento'),
            'sexo': post.get('sexo'),
            'sede': post.get('sede'),
        })
        return request.redirect('/medicos')

    @http.route('/medico/editar/<int:medico_id>', type='http', auth='public', website=True)
    def editar_medico_form(self, medico_id, **kw):
        medico = request.env['medi_serv.medico'].sudo().browse(medico_id)
        return request.render('medi_serv.editar_medico', {'medico': medico})

    @http.route('/medico/actualizar/<int:medico_id>', type='http', auth='public', website=True, csrf=False)
    def actualizar_medico(self, medico_id, **post):
        medico = request.env['medi_serv.medico'].sudo().browse(medico_id)
        medico.write({
            'name': post.get('name'),
            'apellidos': post.get('apellidos'),
            'especialidad': post.get('especialidad'),
            'telefono': post.get('telefono'),
            'email': post.get('email'),
            'fecha_nacimiento': post.get('fecha_nacimiento'),
            'sexo': post.get('sexo'),
            'sede': post.get('sede'),
        })
        return request.redirect('/medicos')
