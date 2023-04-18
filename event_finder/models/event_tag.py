from odoo import fields,models

class EventTag(models.Model):
    _name='event.tag'

    name = fields.Char("Name", required=True, translate=True)
    sequence = fields.Integer('Sequence', default=0)
    category_id = fields.Many2one("event.tag.category")
    category_sequence = fields.Integer(related='category_id.sequence',store=True)
    color = fields.Integer()

    _sql_constraints=[('name_unique','UNIQUE(name)','Same tag cannot be genrated twice')]