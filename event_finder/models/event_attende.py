from odoo import fields,models

class EventAttende(models.Model):
    _name="event.attende"
    _inherit="event.registration"
    
    name= fields.Char(required=True)
    phone_No= fields.Integer(required=True)
    
