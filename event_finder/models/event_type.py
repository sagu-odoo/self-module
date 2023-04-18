from odoo import models,fields,api

class EventType(models.Model):
    _name = 'event.type'
    _description = 'Event Template'

    name = fields.Char('Event Template', required=True, translate=True)
    note = fields.Html(string='Note')
    sequence = fields.Integer()
    # tickets
    event_type_ticket_ids = fields.One2many('event.type.ticket', 'event_type_id', string='Tickets')
    tag_ids = fields.Many2many('event.tag', string="Tags")
    # registration
    has_seats_limitation = fields.Boolean('Limited Seats')
    seats_max = fields.Integer(
        'Maximum Registrations', compute='_compute_seats_max',
        readonly=False, store=True)
    auto_confirm = fields.Boolean(
        'Automatically Confirm Registrations')
    # default_timezone = fields.Selection( string='Timezone', default=lambda self: self.env.user.tz or 'UTC')

    # ticket reports
    # ticket_instructions = fields.Html('Ticket Instructions', translate=True,
    #     help="This information will be printed on your tickets.")
    

    @api.depends('has_seats_limitation')
    def _compute_seats_max(self):
        for template in self:
            if not template.has_seats_limitation:
                template.seats_max = 0