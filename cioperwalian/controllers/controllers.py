# -*- coding: utf-8 -*-
from odoo import http
#from cioperwalian.models.models import MTPerwalianSimple


# class Cioperwalian(http.Controller):
#     @http.route('/cioperwalian/cioperwalian/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cioperwalian/cioperwalian/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cioperwalian.listing', {
#             'root': '/cioperwalian/cioperwalian',
#             'objects': http.request.env['cioperwalian.cioperwalian'].search([]),
#         })

#     @http.route('/cioperwalian/cioperwalian/objects/<model("cioperwalian.cioperwalian"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cioperwalian.object', {
#             'object': obj
#         })


class Perwalians(http.Controller):

    @http.route('/cioperwalian/perwalians', auth='user')
    def list(self, **kwargs):
        MTPerwalianSimple = http.request.env['cioperwalian.mtperwaliansimple']
        perwalians = MTPerwalianSimple.search([])
        return http.request.render(
            'cioperwalian.perwalian_list_template',
            {'perwalians': perwalians})
