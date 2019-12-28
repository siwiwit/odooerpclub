# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class cioacademic(models.Model):
#     _name = 'cioacademic.cioacademic'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class MMAcademicPeriod (models.Model):
    
    _name = 'cioacademic.mmacademicperiod'
    _description = 'Academic Period'
    name = fields.Char('Period Name',translate=True, required=True)
    active = fields.Boolean('Active')
    code = fields.Char('Period Code')
    year = fields.Integer('Period Year')
    year = fields.Integer('Period Year')


class MMAcademicStudent (models.Model):
        
    _name = 'cioacademic.mmacademicstudent'
    _description = 'Academic Student'
    name = fields.Char('Student Name')
    code = fields.Text('Student Code')

class MMAcademicOrganization (models.Model):
        
    _name = 'cioacademic.mmacademicorganization'
    _description = 'Academic Organization'
    name = fields.Char('Organizaton Name')
    code = fields.Text('Organizaton Code')



