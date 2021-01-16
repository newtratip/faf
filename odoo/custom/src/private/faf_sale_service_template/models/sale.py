# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    service_include_id = fields.Many2one(
        comodel_name="sale.service.template",
        string="Service Include",
        compute="_compute_service_include_id",
    )
    service_exclude_id = fields.Many2one(
        comodel_name="sale.service.template",
        string="Service Exclude",
        compute="_compute_service_exclude_id",
    )

    def _compute_service_include_id(self):
        Template = self.env["sale.service.template"]
        for rec in self:
            service_include_id = (
                self.env["ir.config_parameter"]
                .sudo()
                .get_param("sale.service_include_id")
            )
            template = Template.search([("id", "=", int(service_include_id))])
            rec.service_include_id = template.id

    def _compute_service_exclude_id(self):
        Template = self.env["sale.service.template"]
        for rec in self:
            service_exclude_id = (
                self.env["ir.config_parameter"]
                .sudo()
                .get_param("sale.service_exclude_id")
            )
            template = Template.search([("id", "=", int(service_exclude_id))])
            rec.service_exclude_id = template.id
