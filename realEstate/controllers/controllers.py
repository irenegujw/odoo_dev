from odoo import http
from odoo.http import request
from odoo.http import route


class RealEstateController(http.Controller):
    @http.route('/RealEstate/Properties', type='http', auth='public', website=True)
    def display_properties(self, **kw):
        return "realEstate"
