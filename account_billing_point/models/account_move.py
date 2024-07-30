# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015, Eska Yazılım ve Danışmanlık A.Ş.
#    http://www.eskayazilim.com.tr
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

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def _default_billing_point(self):
        company_id = self._context.get('company_id',
                                       self.env.user.company_id.id)
        if self.env.user.default_billing_point_id and \
            self.env.user.default_billing_point_id.company_id.id == company_id:
            return self.env.user.default_billing_point_id
        else:
            return self.env.user.company_id.default_billing_point_id

    billing_point_id = fields.Many2one(
        'account.billing.point',
        'Billing Point',
        readonly=True,
        states={'draft': [('readonly', False)]},
        index=True,
        default=_default_billing_point)

