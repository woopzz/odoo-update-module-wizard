{
    'name': 'Update module wizard',

    'version': '1.1',
    'category': 'Other',
    'author': 'woopzzz',
    'license': 'LGPL-3',
    'auto_install': False,
    'installable': True,
    'application': False,

    'demo': [],

    'depends': [
        'base',
        'web_enterprise',
    ],

    'data': [
        'security/ir.model.access.csv',
        'wizards/ir_module_update.xml',
    ],
}
