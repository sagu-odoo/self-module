from odoo import fields,models

class EventType(models.Model):
    _name="event.type"
    _description=""

    name = fields.Char(required=True)
    