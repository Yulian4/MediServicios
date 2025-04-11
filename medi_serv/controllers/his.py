from odoo import http
from odoo.http import request

class HistoriaClinicaController(http.Controller):

    @http.route('/historia_clinica/lista', auth='public', website=True, csrf=False)
    def lista_historias(self, **kw):
        historias = request.env['medi_serv.historia_clinica'].sudo().search([])
        return request.render('medi_serv.historia_clinica_list', {
            'historias': historias
        })

    @http.route('/historia_clinica/nueva', auth='public', website=True, csrf=False)
    def nueva_historia(self, **kw):
        pacientes = request.env['medi_serv.paciente'].sudo().search([])
        medicos = request.env['medi_serv.medico'].sudo().search([])
        return request.render('medi_serv.crear_historia_clinica', {
            'pacientes': pacientes,
            'medicos': medicos
        })

    @http.route('/historia_clinica/guardar', auth='public', website=True, csrf=False, type='http')
    def guardar_historia(self, **post):
        request.env['medi_serv.historia_clinica'].sudo().create({
            'cod_historia': post.get('cod_historia'),
            'id_pac': int(post.get('id_pac')),
            'nomb_med': int(post.get('nomb_med')),
            'motivo_consulta': post.get('motivo_consulta'),
        })
        return request.redirect('/historia_clinica/list')

    @http.route('/historia_clinica/editar/<int:historia_id>', auth='public', website=True, csrf=False)
    def editar_historia(self, historia_id, **kw):
        historia = request.env['medi_serv.historia_clinica'].sudo().browse(historia_id)
        return request.render('medi_serv.editar_historia_clinica', {
            'historia': historia
        })

    @http.route('/historia_clinica/actualizar/<int:historia_id>', auth='public', website=True, csrf=False, type='http')
    def actualizar_historia(self, historia_id, **post):
        historia = request.env['medi_serv.historia_clinica'].sudo().browse(historia_id)
        historia.write({
            'cod_historia': post.get('cod_historia'),
            'motivo_consulta': post.get('motivo_consulta'),
        })
        return request.redirect('/historia_clinica/list')
