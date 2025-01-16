# -*- coding: utf-8 -*-
from odoo import models, fields

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(string="Nombre y apellidos", required=True)
    license_number = fields.Char(string="Número de colegiado", required=True)
    visits = fields.One2many('hospital.medical.visit', 'doctor_id', string="Visitas")

