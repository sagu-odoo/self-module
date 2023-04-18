from odoo import fields,models


class EventTagCategory(models.Model):
    _name = "event.tag.category"
    _description = "Event Tag Category"
    _order = "sequence"

    name = fields.Char("Name", required=True, translate=True)
    sequence = fields.Integer('Sequence')
    tag_ids = fields.One2many('event.tag', 'category_id', string="Tags")