from odoo import models, fields

class MedicalVisit(models.Model):
    _name = 'hospital.medical.visit'
    _description = 'Medical Visit'

    patient_id = fields.Many2one('hospital.patient', string="Pacient", required=True)
    doctor_id = fields.Many2one('hospital.doctor', string="Metge", required=True)
    diagnosis = fields.Text(string="Diagnostico", required=True)
    date = fields.Datetime(string="Data", default=fields.Datetime.now)

