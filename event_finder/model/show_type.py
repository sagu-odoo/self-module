from odoo import fields,models

class ShowType(models.Model):
    _name='show_type'
    _description=''

    name=fields.Char(required=True)
    