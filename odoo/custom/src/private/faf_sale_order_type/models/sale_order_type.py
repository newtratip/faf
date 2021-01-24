# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class SaleOrderType(models.Model):
    _inherit = "sale.order.type"

    sale_order_template_id = fields.Many2one(
        comodel_name="sale.order.template",
        string="Quotation Template",
    )
