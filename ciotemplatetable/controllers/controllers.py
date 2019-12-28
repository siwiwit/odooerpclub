# -*- coding: utf-8 -*-
from odoo import http

# class Ciotemplatetable(http.Controller):
#     @http.route('/ciotemplatetable/ciotemplatetable/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ciotemplatetable/ciotemplatetable/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ciotemplatetable.listing', {
#             'root': '/ciotemplatetable/ciotemplatetable',
#             'objects': http.request.env['ciotemplatetable.ciotemplatetable'].search([]),
#         })

#     @http.route('/ciotemplatetable/ciotemplatetable/objects/<model("ciotemplatetable.ciotemplatetable"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ciotemplatetable.object', {
#             'object': obj
#         })