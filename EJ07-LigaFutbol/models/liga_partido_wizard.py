# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LigaPartidoWizard(models.TransientModel):
    _name = 'liga.partido.wizard'
    _description = 'Wizard para crear partidos'

    # Campos del wizard
    equipo_casa = fields.Many2one(
        'liga.equipo',
        string='Equipo Local',
        required=True
    )
    equipo_fuera = fields.Many2one(
        'liga.equipo',
        string='Equipo Visitante',
        required=True
    )
    goles_casa = fields.Integer(
        string='Goles Locales',
        default=0
    )
    goles_fuera = fields.Integer(
        string='Goles Visitantes',
        default=0
    )

    def create_match(self):
        """
        Crea un nuevo partido con los datos proporcionados en el wizard.
        """
        # Validar que los equipos no sean el mismo
        if self.equipo_casa == self.equipo_fuera:
            raise ValidationError('El equipo local y el visitante no pueden ser el mismo.')

        # Crear un nuevo registro en el modelo liga.partido
        self.env['liga.partido'].create({
            'equipo_casa': self.equipo_casa.id,
            'equipo_fuera': self.equipo_fuera.id,
            'goles_casa': self.goles_casa,
            'goles_fuera': self.goles_fuera,
        })

