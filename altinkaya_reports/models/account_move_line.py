# Copyright 2023 Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
# from odoo import models, fields, api
#
# TODO: This model file has a function definition that needs to be reworked
#
# class AccountTax(models.Model):
#     _inherit = "account.tax"
#
#     account_id = fields.Many2one(string="Account",
#                                  comodel_name='account.account',
#                                  domain="[('deprecated', '=', False), ('company_id', '=', company_id), ('account_type', 'not in', ('asset_receivable', 'liability_payable', 'off_balance'))]",
#                                  check_company=True,
#                                  help="Account on which to post the tax amount")
#
#
#
# class AccountMoveLine(models.Model):
#     _inherit = "account.move.line"
#
#     kdv_amount = fields.Monetary(
#         default=0.0,
#         currency_field="company_currency_id",
#         string="Amount Total Currency",
#         compute="_compute_kdv_amount",
#         store=True,
#         help="Total amount in company currency."
#         " We use this field in account reporting.",
#     )
#
#     @api.depends(
#         "move_id.date_invoice",
#         "move_id.currency_id",
#         "move_id.custom_rate",
#         "move_id.move_type",
#         "tax_line_id",
#         "price_subtotal",
#     )
#     def _compute_kdv_amount(self):
#         for ail in self:
#             currency_rate = ail.move_id.custom_rate
#             kdv_amount = 0.0
#             for tax in ail.tax_line_id:
#                 # We need to select tax_code based on invoice type
#                 if ail.move_id.move_type in ["out_refund", "in_refund"]:
#                     tax_code = tax.refund_account_id.code
#                 else:
#                     tax_code = tax.account_id.code
#
#                 if tax_code and tax_code.startswith("191.0"):
#                     kdv_amount -= ail.price_subtotal * tax.amount / 100
#                 elif tax_code and tax_code.startswith("391.0"):
#                     kdv_amount += ail.price_subtotal * tax.amount / 100
#
#             # Convert to company currency
#             if ail.currency_id != ail.company_currency_id and currency_rate > 0.00001:
#                 kdv_amount = kdv_amount / currency_rate
#
#             ail.kdv_amount = kdv_amount
#
#
# """
#
# UPDATE
#           account_invoice_line AS ail
#         SET
#           kdv_amount = subquery.total_kdv
#         FROM
#           (
#             SELECT
#               ail.id AS line_id,
#               SUM(
#                 CASE WHEN aa.code LIKE '191.0%' THEN -1 * (
#                   ail.price_subtotal * at.amount / 100
#                 ) WHEN aa.code LIKE '391.0%' THEN ail.price_subtotal * at.amount / 100 ELSE 0 END
#               ) * CASE WHEN rc.id != 31
#               and ai.custom_rate > 0.00001 THEN 1 / ai.custom_rate ELSE 1 END AS total_kdv
#             FROM
#               account_invoice_line AS ail
#               LEFT JOIN account_invoice_line_tax AS ailt ON ail.id = ailt.invoice_line_id
#               LEFT JOIN account_tax AS at ON at.id = ailt.tax_id
#               LEFT JOIN account_account AS aa ON at.account_id = aa.id
#               LEFT JOIN account_invoice AS ai ON ail.move_id = ai.id
#               LEFT JOIN res_currency AS rc ON ai.currency_id = rc.id
#               LEFT JOIN res_currency_rate AS rcr ON rcr.currency_id = rc.id
#               AND rcr.name = ai.date_invoice
#             WHERE
#               aa.code LIKE '191.0%'
#               OR aa.code LIKE '391.0%'
#             GROUP BY
#               ail.id,
#               rc.id,
#               ai.custom_rate
#           ) AS subquery
#         WHERE
#           ail.id = subquery.line_id;
#
#
# """
