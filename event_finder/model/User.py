from odoo import fields,models

class User(models.Model):
    _name="user"
    _description=""

    name = fields.Char(required=True)
    email = fields.Char(required=True)
    phone_number = fields.Integer()