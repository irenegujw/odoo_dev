from odoo import http
from odoo.http import request
from odoo.http import route


class RealEstateController(http.Controller):
    @http.route('/RealEstate',type='http', auth='public',website=True)
    def index(self,**kwargs):
        return "RealEstate"
