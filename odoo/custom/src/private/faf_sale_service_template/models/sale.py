# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    service_template_id = fields.Many2one(
        comodel_name="sale.service.template",
        string="Service Template",
        index=True,
        ondelete="restrict",
    )
