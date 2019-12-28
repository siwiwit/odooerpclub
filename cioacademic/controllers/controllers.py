# -*- coding: utf-8 -*-
from odoo import http

# class Cioacademic(http.Controller):
#     @http.route('/cioacademic/cioacademic/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cioacademic/cioacademic/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cioacademic.listing', {
#             'root': '/cioacademic/cioacademic',
#             'objects': http.request.env['cioacademic.cioacademic'].search([]),
#         })

#     @http.route('/cioacademic/cioacademic/objects/<model("cioacademic.cioacademic"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cioacademic.object', {
#             'object': obj
#         })