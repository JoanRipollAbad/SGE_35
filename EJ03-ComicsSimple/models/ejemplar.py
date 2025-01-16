from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class BibliotecaEjemplar(models.Model):
    _name = 'biblioteca.ejemplar'
    _description = 'Ejemplar de Cómic para Préstamo'

    comic_id = fields.Many2one('biblioteca.comic', string="Cómic", required=True)
    socio_id = fields.Many2one('biblioteca.socio', string="Socio", required=True)
    fecha_inicio = fields.Date(string="Fecha de Inicio", required=True)
    fecha_fin = fields.Date(string="Fecha de Fin", required=True)

    @api.constrains('fecha_inicio', 'fecha_fin')
    def _check_fechas(self):
        for record in self:
            if record.fecha_inicio > date.today():
                raise ValidationError("La fecha de inicio no puede ser posterior al día de hoy.")
            if record.fecha_fin < date.today():
                raise ValidationError("La fecha de fin no puede ser anterior al día de hoy.")

