# -*- coding: utf-8 -*-
# from odoo import http


# class MediServ(http.Controller):
#     @http.route('/medi_serv/medi_serv', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/medi_serv/medi_serv/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('medi_serv.listing', {
#             'root': '/medi_serv/medi_serv',
#             'objects': http.request.env['medi_serv.medi_serv'].search([]),
#         })

#     @http.route('/medi_serv/medi_serv/objects/<model("medi_serv.medi_serv"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('medi_serv.object', {
#             'object': obj
#         })

