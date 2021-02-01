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
    sale_order_type_id = fields.Many2one(
        comodel_name="sale.order.type",
        related="sale_order_id.type_id",
        store=True,
    )
    sale_order_subject = fields.Char(
        related="sale_order_id.subject",
        string="Project Description",
        store=True,
    )
