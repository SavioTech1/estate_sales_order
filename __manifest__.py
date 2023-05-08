{
    'name': 'Estate SaleOrder',
    'version': '14.0.1.0.0',
    'author': 'Savio',
    'category': 'Sales/sales',
    'summary': '',
    'description': "collegamento modulo vendita",
    
    'depends': ['estate','sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_product_views.xml',
        'views/estate_property_views.xml',

    ],
    
    'installable': True
}