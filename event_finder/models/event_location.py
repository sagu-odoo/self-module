from odoo import fields,models

class EventLocation(models.Model):
    _name='event.location'
    event_location_name = fields.Char(required=True)
    event_address=fields.Text()
    event_capacity=fields.Integer(required=True)
    
    event_location_price = fields.Integer()
    event_booking_start = fields.Date()
    event_ending_start = fields.Date()
    

