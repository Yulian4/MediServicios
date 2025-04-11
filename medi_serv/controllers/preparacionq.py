from odoo import http
from odoo.http import request

class PreparacionQController(http.Controller):
    
    @http.route('/medi_serv/preparacionq', auth='user', website=True, csrf=False)
    def list_preparaciones(self):
   
        preparaciones = request.env['medi_serv.preparacion_q'].search([])
        return request.render('medi_serv.preparacionq_list', {
            'preparaciones': preparaciones
        })

    @http.route('/medi_serv/preparacionq/create', auth='user', website=True, csrf=False)
    def create_preparacion(self, **kwargs):
       
        if request.httprequest.method == 'POST':
            paciente_id = kwargs.get('paciente_id')
            descripcion = kwargs.get('descripcion')
            fecha_preparacion = kwargs.get('fecha_preparacion')
            preparacion = request.env['medi_serv.preparacion_q'].create({
                'paciente_id': paciente_id,
                'descripcion': descripcion,
                'fecha_preparacion': fecha_preparacion,
                'estado': 'pendiente'
            })
            return request.redirect('/medi_serv/preparacionq')

       
        pacientes = request.env['medi_serv.paciente'].search([])
        return request.render('medi_serv.preparacionq_form', {
            'pacientes': pacientes
        })
