from odoo import fields,models

class EventTicket(models.Model):
    _name='ef.event.ticket'
    _inherit=['event.type.ticket','event.event.ticket']
    ticket_quantity=fields.Integer(default=1)
    ticket_type=fields.Selection([('classic','Classic'),('premium','Premium')])
    
