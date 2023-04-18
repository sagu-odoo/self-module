from odoo import fields,models

class EventAttende(models.Model):
    _name="event.attende"
    # _inherit="event.attende"
     #  attende
    partner_id = fields.Many2one('res.partner')
    name = fields.Char(required=True)
    email = fields.Char()
    phone = fields.Char()
    mobile = fields.Char()
    
