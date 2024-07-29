# -*- coding: utf-8 -*-
{
    'name': 'Invoice Currency Rate',
    'version': '16.0.0.1.0',
    'category': 'Accounting',
    'summary': 'Invoice Currency Rate',
    'author': 'Codequarters - KOD MERKEZİ Yazılım ve İnternet Hizmetleri Eğitim Danışmanlık LTD. Şti.',
    'website': 'https://www.codequarters.com',
    'description': """
Invoice Currency Rate
====================================================

Setting the currency rate you want to force on invoice.

    """,
    'depends': [
        "account",
    ],
    'data': [
        'views/account_move_views.xml'
    ],
    'installable': True,
}
