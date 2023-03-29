from odoo import fields,models,api,exceptions

class EventProperty(models.Model):
    _name='event.property'
    _description='Events Details'

    name=fields.Char(required=True)
    place=fields.Char(required=True)
    description=fields.Text(required=True) 
    date=fields.Text(required=True)
    event_type_id = fields.Many2many("event.type","relationalfield")
    
    
