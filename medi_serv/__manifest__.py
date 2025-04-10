# -*- coding: utf-8 -*-
{
    'name': "mediServ",

    'summary': "Modulo de atención médica Clínica del Parque.",

    'description': """
Modulo en Odoo que integra el flujo completo de atención médica de la Clínica del Parque, desde el ingreso del paciente hasta el alta y facturación, incluyendo soporte a decisiones clínicas, automatización de tareas, y estrategias de captación de clientes.
    """,

    'author': "Julian Gordillo / Yuliana Yate / Alexis Rodriguez",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        #'views/views.xml',
        'views/templates.xml',
        'views/insumos.xml',
        'views/medicamentos.xml',
        'views/pacientes.xml',
        'views/medicos.xml',
        'views/habitaciones.xml',
        'views/preparacionq.xml',
        'views/facturas.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

