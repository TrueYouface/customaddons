# -*- coding: utf-8 -*-

from odoo import models


class ResCurrency(models.Model):
    _inherit = 'res.currency'

    def _get_rates(self, company, date):
        result = super(ResCurrency, self)._get_rates(company, date)

        use_custom_rate = self._context.get('use_custom_rate',False)
        custom_rate_currency_id = self._context.get('custom_rate_currency_id', False)

        for rate in self:
            if use_custom_rate and rate.id == custom_rate_currency_id:
                result[rate.id] = self._context.get('custom_rate', False)

        return result
