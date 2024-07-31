# -*- coding: utf-8 -*-
'''
@author: Codequarters - Grey
'''

from odoo import models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    invoice_bank_ids = fields.Many2many(
        'res.partner.bank', string='Bank Accounts',
        help='Bank Account Number to which the invoice will be paid. Default bank accounts in a Customer Invoice',
        domain="[('partner_id', '=', partner_id)]")
