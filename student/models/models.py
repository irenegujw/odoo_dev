# -*- coding: utf-8 -*-

from odoo import models, fields, api


class School(models.Model):
    _name = 'odoo.school'
    _description = 'School'
    name = fields.Char('Name')
    student_list = fields.One2many('odoo.student', 'school_id', string='Student List')
    ref_field_id = fields.Reference([('odoo.school', 'School'),
                                     ('odoo.student', 'Student'),
                                     ('odoo.hobby', 'hobby'),
                                     ('sale.order', 'order'),
                                     ('account.move', 'Reference Reference'),
                                     ], string='Reference Field')


class Hobby(models.Model):
    _name = 'odoo.hobby'
    _description = 'Hobby dec'
    name = fields.Char('Hobby')


class Student(models.Model):
    _name = 'odoo.student'  # psql database name is odoo.student
    _description = 'This is student model'

    hobby_list = fields.Many2many('odoo.hobby',
                                  'student_hobby_list_relation',
                                  "student_id",
                                  "hobby_id")
    school_id = fields.Many2one('odoo.school', 'School id', default=1, index=True)

    name = fields.Char("Name")
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')],
    )

    advance_gender = fields.Selection("_get_gender_list", default='male')

    def _get_gender_list(self):
        return [('male', 'Male'), ('female', 'Female'), ('1', '1')]

    @api.model
    def _get_vip_list(self):
        return [('a', '1'), ('b', '2'), ('c', '3'), ]

    vip_gender = fields.Selection(_get_vip_list)

    roll_number = fields.Integer("Roll Number")

    # school_data = fields.Json()
    #
    # def json_data_store(self):
    #     self.school_data = {"name": self.name, "roll_number": self.roll_number, "g": self.gender}

    name1 = fields.Char("Name1", tracking=True, translate=True)
    name2 = fields.Char("Name2", copy=False)
    name3 = fields.Char("Name3", default='default value', )
    name4 = fields.Char("Name4", readonly=True)

    student_name = fields.Char(string='Student', required=True, index=True, size=5)
    address = fields.Text(string='Address')
    address_html = fields.Html(string='Html field',
                               tracking=True,
                               default="<h1>This is Default in h1</h1>")
