from odoo import fields,models

class EventEvent(models.Model):
    _name='in.event.event'
    _inherit=['event.event']
    name=fields.Char()
    description=fields.Text()
    date_of_event= fields.Date()
    event_type_ids = fields.Many2many('event.tag')
    start_time =fields.Date(required=True)
    end_time=fields.Date(required=True)
    event_location_id=fields.Many2one('event.location')
    ticket_type = fields.Char() 
    ticket_price=fields.Float()
    


