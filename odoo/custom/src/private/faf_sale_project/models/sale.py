# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    project_description = fields.Html(
        compute="_compute_project_description",
        string="Project Description",
        store=True,
    )
    project_status = fields.Char(
        compute="_compute_project_status",
        string="Project Status",
        store=True,
    )

    @api.depends("project_ids", "project_ids.description")
    def _compute_project_description(self):
        for order in self:
            order.project_description = ", ".join(
                filter(lambda l: l, order.project_ids.mapped("description"))
            )

    @api.depends("project_ids", "project_ids.project_status")
    def _compute_project_status(self):
        for order in self:
            order.project_status = ", ".join(
                filter(lambda l: l, order.project_ids.mapped("project_status.name"))
            )
