from odoo import models, fields

class BibliotecaComic(models.Model):
    _name = 'biblioteca.comic'
    _description = 'Cómics de la Biblioteca'

    nombre = fields.Char(string="Título", required=True)
    autor = fields.Char(string="Autor", required=True)
    genero = fields.Char(string="Género")
    publicacion = fields.Date(string="Fecha de Publicación")
    
    
