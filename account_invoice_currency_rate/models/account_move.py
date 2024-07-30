# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def _default_currency_rate(self):
        currency = self.env['res.company']._default_currency_id()
        # if self.partner_id.property_rate_field != "rate":
        #     rate = currency.second_rate
        # else:
        #     rate = currency.rate
        rate = currency.with_context(
            rate_field=self.partner_id.property_rate_field
        ).rate
        return rate or 1.0

    currency_rate = fields.Float('Currency Rate', digits=(12, 4), default=_default_currency_rate)
    currency_rate_related = fields.Float(
        related='currency_rate', help="Technical field for readonly", readonly=False, digits=(12, 4))
    use_custom_rate = fields.Boolean('Custom Currency Rate', default=False)
    foreign_currency = fields.Boolean('Foreign Currency', compute='_compute_foreign_currency', store=True)


    @api.depends('currency_id', 'company_id')
    def _compute_foreign_currency(self):
        for move in self:
            move.foreign_currency = move.currency_id != move.company_id.currency_id or False


    def onchange(self, values, field_name, field_onchange):
        new_context = self._context.copy()
        if 'use_custom_rate' in values and 'currency_rate' in values and 'currency_id' in values:
            new_context.update({
                'use_custom_rate': values['use_custom_rate'],
                'custom_rate': values['currency_rate'],
                'custom_rate_currency_id': values['currency_id']
            })
        return super(AccountMove, self.with_context(new_context)).onchange(values, field_name, field_onchange)

    @api.onchange('currency_rate', 'use_custom_rate', 'currency_id', 'date_invoice')
    def _onchange_currency(self):
        if not self.currency_id or self.currency_id == self.company_id.currency_id:
            self.currency_rate = 1.0
            self.use_custom_rate = False
        elif not self.use_custom_rate:
            company = self.company_id or self.env.user.company_id
            if self.partner_id and self.partner_id.property_rate_field != "rate":
                self = self.with_context(
                    rate_type=self.partner_id.property_rate_field
                )
            rate = self.env['res.currency']._get_conversion_rate(
                self.currency_id, company.currency_id, company, self.date_invoice or fields.Date.today())
            self.currency_rate = rate
        else:
            self.custom_rate = 1 / self.currency_rate


    def action_move_create(self):
        new_context = self._context.copy()
        if self.use_custom_rate and self.currency_rate:
            new_context.update({
                'use_custom_rate': self.use_custom_rate,
                'custom_rate': 1 / self.currency_rate,
                'custom_rate_currency_id': self.currency_id.id
            })
        return super(AccountMove, self.with_context(new_context)).action_move_create()
