# -*- coding: utf-8 -*-
{
    'name': 'Gestión de Ciclos Formativos',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Gestión de ciclos formativos, módulos, alumnos y profesores en un instituto.',
    'author': 'Tu Nombre',
    'depends': ['base'],
    'data': [
    	'security/groups.xml',
        'security/ir.model.access.csv',
        'views/ciclo_view.xml',
    ],
    'installable': True,
    'application': True,
}

