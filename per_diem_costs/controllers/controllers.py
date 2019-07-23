# -*- coding: utf-8 -*-
from odoo import http

# class PerDiemCosts(http.Controller):
#     @http.route('/per_diem_costs/per_diem_costs/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/per_diem_costs/per_diem_costs/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('per_diem_costs.listing', {
#             'root': '/per_diem_costs/per_diem_costs',
#             'objects': http.request.env['per_diem_costs.per_diem_costs'].search([]),
#         })

#     @http.route('/per_diem_costs/per_diem_costs/objects/<model("per_diem_costs.per_diem_costs"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('per_diem_costs.object', {
#             'object': obj
#         })