from odoo import models, fields

class Profesor(models.Model):
    _name = 'profesor.instituto'
    _description = 'Profesor'

    name = fields.Char(string="Nombre del Profesor", required=True)
    modulo_ids = fields.One2many('modulo.formativo', 'profesor_id', string="Módulos Impartidos")

