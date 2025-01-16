from odoo import models, fields

class ModuloFormativo(models.Model):
    _name = 'modulo.formativo'
    _description = 'Módulo Formativo'

    name = fields.Char(string="Nombre del Módulo", required=True)
    ciclo_id = fields.Many2one('ciclo.formativo', string="Ciclo Formativo", required=True)
    alumno_ids = fields.Many2many('alumno.instituto', string="Alumnos Matriculados")
    profesor_id = fields.Many2one('profesor.instituto', string="Profesor")

