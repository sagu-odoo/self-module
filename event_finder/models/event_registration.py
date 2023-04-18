from odoo import models,fields

class EventRegistration(models.Model):
    _name ='event.registration'
     
    event_id = fields.Many2one(
        'event.event')
    # event_ticket_id = fields.Many2one(
    #     'event.ticket')
    active = fields.Boolean(default=True)

    partner_id = fields.Many2one('res.partner')
    name = fields.Char()
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    mobile = fields.Char(string='Mobile')
   
    date_closed = fields.Datetime()
    event_begin_date = fields.Datetime()
    event_end_date = fields.Datetime()
    # event_organizer_id = fields.Many2one()
    # event_user_id = fields.Many2one('event_id.user_id')
    state = fields.Selection([
        ('draft', 'Unconfirmed'), ('cancel', 'Cancelled'),
        ('open', 'Confirmed'), ('done', 'Attended')])
