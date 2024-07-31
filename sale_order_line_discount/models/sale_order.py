# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    unit_discounted = fields.Float('Disc. Unit',
                                   digits=dp.get_precision('Product Price'),
                                   compute='_compute_unit_discounted',
                                   readonly=True, states={'draft': [('readonly', False)]},
                                   store=True)

    @api.depends('price_unit', 'discount')
    def _compute_unit_discounted(self):
        for rec in self:
            rec.unit_discounted = rec.price_unit * ((100.0 -rec.discount) / 100.0)


