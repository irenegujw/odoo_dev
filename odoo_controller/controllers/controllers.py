# -*- coding: utf-8 -*-
from odoo import http

class OdooController(http.Controller):
    @http.route('/odoo_controller/odoo_controller/', auth='public')
    def index(self, **kw):
        try:
            sales_orders = http.request.env['sale.order'].search([])
            # make sure you !installed! the sale module!!
        except :
            return "can't access sales orders"

        output = "<h1>:::Sales Orders:::</h1><ul>"
        for sale in sales_orders:
            output += "<li>%s</li>" % sale['name']
            print(sale['name'])
        output += "</ul>"
        return output + "<h1>Data Accessed</h1>"

#     @http.route('/odoo_controller/odoo_controller/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_controller.listing', {
#             'root': '/odoo_controller/odoo_controller',
#             'objects': http.request.env['odoo_controller.odoo_controller'].search([]),
#         })

#     @http.route('/odoo_controller/odoo_controller/objects/<model("odoo_controller.odoo_controller"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_controller.object', {
#             'object': obj
#         })
