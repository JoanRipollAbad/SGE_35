# -*- coding: utf-8 -*-
from odoo import models, fields

class Alumno(models.Model):
    _name = 'alumno.instituto'
    _description = 'Alumno'

    name = fields.Char(string="Nombre del Alumno", required=True)
    modulo_ids = fields.Many2many('modulo.formativo', string="Módulos Matriculados")

