# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013-Today Acespritech Solutions Pvt Ltd
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
    'name': 'Partner Doviz Statement',
    'author': 'yigit budak',
    'website': 'https://github.com/yibudak',
    'version': '1.0',
    'category': 'Account',
    'description': """
Calculate partner statement with secondary currency
    """,
    'depends': ['base', 'account'],
    "update_xml": [
        "wizard/partner_doviz_statement_wizard_view.xml",
        "views/res_partner_view.xml"
    ],
    'installable': True,
}
