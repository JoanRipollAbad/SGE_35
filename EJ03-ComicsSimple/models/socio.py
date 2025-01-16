from odoo import models, fields

class BibliotecaSocio(models.Model):
    _name = 'biblioteca.socio'
    _description = 'Socios de la Biblioteca'

    nombre = fields.Char('Nombre', required=True)
    apellido = fields.Char('Apellido', required=True)
    identificador = fields.Char('Identificador', required=True, unique=True)

