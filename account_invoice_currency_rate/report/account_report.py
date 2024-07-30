# -*- coding: utf-8 -*-
'''
@author: Codequarters - Grey
'''

from odoo import models, fields, api, tools


class AccountReport(models.Model):
    _inherit = "account.report"

    currency_rate = fields.Float(digits=(12,4))

    def _select(self):
        return super(AccountReport, self)._select().replace("COALESCE(cr.rate, 1)","COALESCE(sub.currency_rate, 1)")

    def _sub_select(self):
        return super(AccountReport, self)._sub_select() + ", ai.currency_rate as currency_rate"


    def init(self):
        # self._table = account_invoice_report
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (
                %s
                FROM (
                    %s %s WHERE ail.account_id IS NOT NULL %s
                ) AS sub
            )""" % (
            self._table, self._select(), self._sub_select(), self._from(), self._group_by()))
