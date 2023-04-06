from odoo import fields,models

class EventLocation(models.Model):
    _name='event.location'
    name = fields.Char(required=True)
    address=fields.Text()
    capacity=fields.Integer(required=True)
    event_id=fields.One2many('event.event','event_location_id')
    