# -*- coding: utf-8 -*-
from odoo import models, fields

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Nombre y Apellidos', required=True)
    sintomas = fields.Text(string='Síntomas')
    visits = fields.One2many('hospital.medical.visit', 'patient_id', string="Visitas")

