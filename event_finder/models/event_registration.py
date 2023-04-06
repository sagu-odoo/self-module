from odoo import models,fields

class EventRegistration(models.Model):
    _name ='event.registration'
    

    attende=fields.Many2many()