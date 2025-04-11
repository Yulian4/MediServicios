from odoo import http
from odoo.http import request

class FacturaController(http.Controller):

    @http.route(['/factura/<int:factura_id>'], type='http', auth='user', website=True)
    def ver_factura(self, factura_id, **kw):
        factura = request.env['medi_serv.factura'].sudo().browse(factura_id)
        if not factura.exists():
            return request.not_found()

        medicamentos = []
        preparaciones = request.env['medi_serv.preparacion_q'].sudo().search([
            ('paciente_id', '=', factura.paciente_id.id)
        ])
        for prep in preparaciones:
            for linea in prep.medicamento_line_ids:
                if linea.medicamento_id:
                    medicamentos.append({
                        'codigo': linea.medicamento_id.codigo,
                        'nombre': linea.medicamento_id.name,
                        'principio_activo': linea.medicamento_id.principio_activo,
                        'forma_farmaceutica': linea.medicamento_id.forma_farmaceutica,
                        'concentracion': linea.medicamento_id.concentracion,
                        'via_administracion': linea.medicamento_id.via_administracion,
                        'dosis_recomendada': linea.medicamento_id.dosis_recomendada,
                        'precio': linea.medicamento_id.precio,
                    })

        return request.render('medi_serv.vista_factura_detalle', {
            'factura': factura,
            'medicamentos': medicamentos
        })
