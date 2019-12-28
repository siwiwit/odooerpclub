# -*- coding: utf-8 -*-
from odoo import http

# class Ciobase(http.Controller):
#     @http.route('/ciobase/ciobase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ciobase/ciobase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ciobase.listing', {
#             'root': '/ciobase/ciobase',
#             'objects': http.request.env['ciobase.ciobase'].search([]),
#         })

#     @http.route('/ciobase/ciobase/objects/<model("ciobase.ciobase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ciobase.object', {
#             'object': obj
#         })