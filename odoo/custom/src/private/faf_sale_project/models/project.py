# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    date_sale_order = fields.Datetime(
        related="sale_order_id.date_order",
        string="Sale Order Date/Project Date",
        store=True,
    )
