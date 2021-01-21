# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    service_template_id = fields.Many2one(
        comodel_name="sale.service.template",
        string="Service Template",
        index=True,
        ondelete="restrict",
    )
    service_include_description = fields.Html()
    service_exclude_description = fields.Html()

    @api.onchange("service_template_id")
    def _onchange_service_template_id(self):
        self.service_include_description = (
            self.service_template_id.service_include_description
        )
        self.service_exclude_description = (
            self.service_template_id.service_exclude_description
        )
