# Copyright 2021 Ecosoft Co., Ltd (http://ecosoft.co.th)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _prepare_invoice_values(self, order, name, amount, so_line):
        vals = super()._prepare_invoice_values(order, name, amount, so_line)
        vals["salesperson_id"] = order.salesperson_id.id
        return vals
