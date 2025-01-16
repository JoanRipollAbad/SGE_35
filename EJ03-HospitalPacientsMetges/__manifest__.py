# -*- coding: utf-8 -*-
{
    'name': 'Hospital Management',
    'version': '1.0',
    'summary': 'Gestión de pacientes y médicos para un hospital.',
    'sequence': -100,
    'description': """Gestión hospitalaria con pacientes y médicos.""",
    'category': 'Healthcare',
    'author': 'Tu Nombre',
    'website': 'http://www.tuempresa.com',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/hospital_menu.xml',
    ],
    'installable': True,
    'application': True,
}

