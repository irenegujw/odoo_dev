# -*- coding: utf-8 -*-

from odoo import models, fields


class School(models.Model):
    _name = 'odoo.school'  # psql database name is odoo_school
    _description = 'This is school model'

    name = fields.Char("Name")
    student_list = fields.One2many('odoo.student', 'school_id', string='Student List')
    ref_field_id = fields.Reference([('odoo.school', 'School'),
                                     ('odoo.student', 'Student'),
                                     ('odoo.hobby', 'hobby'),
                                     ('sale.order', 'Reference Reference'),
                                     ('account.move', 'Reference Reference'),
                                     ], string='Reference Field')