from odoo import fields,models

class EventEvent(models.Model):
    _name='event.event'
    
    name = fields.Char(string='Event', translate=True, required=True)
    note = fields.Html(string='Note', store=True, compute="_compute_note", readonly=False)
    description = fields.Html(string='Description')
    active = fields.Boolean(default=True)

    organizer_id = fields.Many2one(
        'res.partner', string='Organizer',
        default=lambda self: self.env.company.partner_id
        )
    # event_type_id = fields.Many2one('event.type', string='Template')
    tag_ids = fields.Many2many(
        'event.tag', string="Tags")
    
    # auto_confirm = fields.Boolean(
    #     string='Autoconfirmation', compute='_compute_auto_confirm', readonly=False, store=True)
    registration_ids = fields.One2many('event.registration', 'event_id', string='Attendees')
    # event_ticket_ids = fields.One2many(
    #     'event.ticket', 'event_id', string='Event Ticket', copy=True,readonly=False, store=True)
    
    # Date fields
    event_date = fields.Date()
    event_location= fields.Char()

    event_start_time = fields.Datetime(string='Start Date', required=True)
    event_end_time = fields.Datetime(string='End Date', required=True)
    # date_begin_located = fields.Char(string='Start Date Located', compute='_compute_date_begin_tz')
    # date_end_located = fields.Char(string='End Date Located', compute='_compute_date_end_tz')

    
    # = fields.Html('Ticket Instructions', readonly=False,
    #     help="This information will be printed on your tickets.")

