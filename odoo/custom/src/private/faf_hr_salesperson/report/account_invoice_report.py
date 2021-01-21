# Copyright 2021 Ecosoft Co., Ltd (http://ecosoft.co.th)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    invoice_user_id = fields.Many2one(
        string="Salesperson (not used)",
    )
    salesperson_id = fields.Many2one(
        comodel_name="hr.employee",
        string="Salesperson",
        readonly=True,
    )

    @api.model
    def _select(self):
        select_str = super()._select()
        select_str += """
            , move.salesperson_id
        """
        return select_str
