from odoo import fields,models

class EventSeatType(models.Model):
    _name = "event.seat.type"
    _description=""

    name=fields.Char(required=True)
    

