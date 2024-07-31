# -*- coding: utf-8 -*-
{
    'name': 'Manual Procurement Priority',

    'summary': """
       Adds priority field to product replenish model.
       """,

    'description': """
        Adds priority field to product replenish model.
    """,

    'author': "yibudak",

    'website': "https://github.com/yibudak",

    'category': 'Product',

    'version': '16.0.1.0.0',

    'depends': ['base', 'mrp', 'stock'],

    'data': [
        'wizard/product_replenishment_view.xml',
    ],
}