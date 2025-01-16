# -*- coding: utf-8 -*-
from odoo import models, fields

class CicloFormativo(models.Model):
    _name = 'ciclo.formativo'
    _description = 'Ciclo Formativo'

    name = fields.Char(string="Nombre del Ciclo", required=True)
    description = fields.Text(string="Descripción")
    modulo_ids = fields.One2many('modulo.formativo', 'ciclo_id', string="Módulos Asociados")

