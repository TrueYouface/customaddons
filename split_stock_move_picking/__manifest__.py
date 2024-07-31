# -*- coding: utf-8 -*-
{
    'name': 'Split Stock Move Picking',

    'summary': """
       Splits stock.move record in pickings.
       """,

    'description': """
       Splits stock.move record in stock.picking model.
    """,

    'author': "yibudak",

    'website': "https://github.com/yibudak",

    'category': 'Product',

    'version': '16.0.1.0.0',

    'depends': ['base', 'stock'],

    'data': [
        # 'wizard/wizard_split_picking_line.xml',
        # 'views/stock_picking_view.xml',
    ],
}