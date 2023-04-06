from odoo import fields,models

class EventTag(models.Model):
    _name='event.tag'
    _inherit=['event.tag.category','event.tag']

    name=fields.Char(required=True)
    color=fields.Integer()

    _sql_constraints=[('name_unique','UNIQUE(name)','Same tag cannot be genrated twice')]