from odoo import fields,models

class EventLocation(models.Model):
    _name="event.location"
    _description=""

    name=fields.Char(required=True)
    address = fields.Char()
    capacity =fields.Integer()
    event_id =fields.Many2one()
    
