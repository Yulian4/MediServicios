from odoo import http
from odoo.http import request

class PacienteController(http.Controller):

    @http.route('/paciente/lista', auth='public', website=True, csrf=False)
    def lista_pacientes(self, **kw):
        pacientes = request.env['medi_serv.paciente'].sudo().search([])
        return request.render('medi_serv.lista_pacientes', {
            'pacientes': pacientes
        })

    @http.route('/paciente/crear', auth='public', website=True, methods=['GET', 'POST'], csrf=False)
    def crear_paciente(self, **post):
        if http.request.httprequest.method == 'POST':
            request.env['medi_serv.paciente'].sudo().create(post)
            return request.redirect('/paciente/lista')
        return request.render('medi_serv.crear_paciente')

    @http.route('/paciente/editar/<int:paciente_id>', auth='public', website=True, methods=['GET', 'POST'], csrf=False)
    def editar_paciente(self, paciente_id, **post):
        paciente = request.env['medi_serv.paciente'].sudo().browse(paciente_id)
        if http.request.httprequest.method == 'POST':
            paciente.sudo().write(post)
            return request.redirect('/paciente/lista')
        return request.render('medi_serv.editar_paciente', {
            'paciente': paciente
        })
