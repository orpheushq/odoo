{
    'name': "Real Estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "Orpheus",
    'category': 'Sales',
    'description': """
    A test Odoo module
    """,
    'application': True,
    # data files always loaded at installation
    'data': [
        'views/mymodule_view.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        'demo/demo_data.xml',
    ],
}