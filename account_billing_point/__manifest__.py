# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2018, Kod Merkezi Yazılım LTD.
#    http://www.codequarters.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Billing Point',
    'version': '16.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Billing Point',
    'description': """
Billing Point
====================================================

Adds selection of billing point on invoices. This can be used to work with billing locations with different conditions.
    """,
    'author': 'Kod Merkezi Yazılım LTD.',
    'website': 'http://www.codequarters.com',
    'depends': ['account'],
    'data': [
        'views/account_move_view.xml',
        'views/account_billing_point_view.xml',
        'views/res_partner_view.xml',
        'views/res_company_view.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
    ],
    'installable': True,
}