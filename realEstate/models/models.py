# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime,timedelta


class RealEstate(models.Model):
    _name = 'odoo.real.estate'  # psql database name is odoo_real_estate
    _description = 'This is real estate model'

    name = fields.Char("Name", required=True)
    description = fields.Text("Description")
    postcode = fields.Char("Postcode")
    date_availability = fields.Date(
        "Date Availability",
        default=lambda self: (datetime.today() + timedelta(days=90)).strftime('%Y-%m-%d')
    )
    # date_availability = fields.Date("Date Availability",default=fields.Date.today)
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", readonly=True, copy=False)
    bedrooms = fields.Integer("Bedrooms",default=2)
    living_area = fields.Integer("Living Area",help="sqft")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area")
    garden_orientation = fields.Selection(
        [('east', 'East'), ('west', 'West'),('north','North'),('south','South')],
        "Garden Orientation")
    active = fields.Boolean("Active",default=True)
    state = fields.Selection(
        [('new', 'New'),
         ('offer_received', 'Offer Received'),
         ('offer_accepted', 'Offer Accepted'),
         ('sold', 'Sold'),
         ('canceled', 'Canceled')],
        string="Status",
        required=True,
        default='new',
        copy=False
)


