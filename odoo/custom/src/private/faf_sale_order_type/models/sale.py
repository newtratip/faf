# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    type_id = fields.Many2one(
        default=False,
    )

    @api.onchange("type_id")
    def _onchange_type_id(self):
        self.sale_order_template_id = self.type_id.sale_order_template_id
