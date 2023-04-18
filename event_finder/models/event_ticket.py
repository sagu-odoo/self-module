from odoo import fields,models

class EventTicket(models.Model):
    _name='event.ticket'
   
    ticket_type = fields.Selection(selection={("classic","Classic"),('standard','Standard'),('premium','Premium')})

    event_name_id = fields.Many2one('event.event')

    ticket_price = fields.Integer()


