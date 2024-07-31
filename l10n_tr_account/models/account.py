# -*- coding: utf-8 -*-
'''
Created on Dec 25, 2019

@author: ugur
'''
from odoo import models, fields, api


class AccountTax(models.Model):
    _inherit = "account.tax"

    is_withholding = fields.Boolean('Is Withholding?', default=False)
    withholding_rate = fields.Float(string='Withholding Rate')
    is_exemption = fields.Boolean('Is Exemption?', default=False)
    is_export_registered = fields.Boolean('Is Export Registered?', default=False)
    exemption_code = fields.Char(string='Exemption Code')
    exemption_reason = fields.Char(string='Exemption Reason')

    @api.onchange('is_withholding')
    def _onchange_is_withholding(self):
        self.is_export_registered = False
        self.is_exemption = False

    @api.onchange('is_exemption')
    def _onchange_is_exemption(self):
        self.is_export_registered = False
        self.is_withholding = False

    @api.onchange('is_export_registered')
    def _onchange_is_export_registered(self):
        self.is_exemption = False
        self.is_withholding = False


class AccountInvoiceLine(models.Model):
    _inherit = 'account.move.line'

    price_tax_withholding = fields.Monetary(string='Withholding Tax Amount', compute='_get_price_tax', store=False)

    def _get_price_tax(self):
        super(AccountInvoiceLine, self)._get_price_tax()
        for line in self:
            amount_withholding = 0
            currency = line.invoice_id and line.invoice_id.currency_id or None
            price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
            taxes = False
            if line.invoice_line_tax_ids:
                taxes = line.invoice_line_tax_ids.compute_all(price, currency, line.quantity, product=line.product_id,
                                                              partner=line.invoice_id.partner_id)

                amount_withholding = sum(t['amount'] for t in taxes['taxes'])

            line.price_tax_withholding = amount_withholding


class AccountInvoice(models.Model):
    _inherit = 'account.move'

    invoice_bank_ids = fields.Many2many(
        'res.partner.bank', string='Bank Accounts',
        help='Bank Account Number to which the invoice will be paid. A Company bank account if this is a Customer Invoice or Vendor Credit Note, otherwise a Partner bank account number.',
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")

    bank_partner_id = fields.Many2one(
        'res.partner', compute='_compute_bank_partner_id', help='Technical field to get the domain on the bank')


    def _set_company_bank_accounts(self):
        for invoice in self.filtered(lambda i: not i.invoice_bank_ids and i.company_id):
            invoice.invoice_bank_ids = invoice.company_id.invoice_bank_ids

    @api.depends('partner_id')
    def _compute_bank_partner_id(self):
        for invoice in self:
            if invoice.type in ['in_invoice', 'out_refund']:
                invoice.bank_partner_id = invoice.partner_id.commercial_partner_id
            else:
                invoice.bank_partner_id = invoice.company_id.partner_id

    @api.model
    def create(self, vals_list):
        invoice = super(AccountInvoice, self).create(vals_list)
        out_invoices = invoice.filtered(lambda invoice: invoice.type in ['out_invoice','in_refund']) 
        out_invoices._set_company_bank_accounts()
        return invoice



