# Copyright 2021 Ecosoft Co., Ltd (http://ecosoft.co.th)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    user_id = fields.Many2one(
        string="Salesperson (not used)",
    )
    salesperson_id = fields.Many2one(
        comodel_name="hr.employee",
        domain=lambda self: self._get_domain_salesperson_id(),
        index=True,
    )

    @api.model
    def _get_domain_salesperson_id(self):
        try:
            return [("department_id", "=", self.env.ref("hr.dep_sales").id)]
        except ValueError:
            return []

    @api.onchange("partner_id")
    def onchange_partner_id(self):
        super().onchange_partner_id()
        if not self.partner_id:
            return
        partner_salesperson = (
            self.partner_id.salesperson_id
            or self.partner_id.commercial_partner_id.salesperson_id
        )
        salesperson_id = partner_salesperson.id
        if salesperson_id and self.salesperson_id.id != salesperson_id:
            self["salesperson_id"] = salesperson_id

    def _prepare_invoice(self):
        res = super()._prepare_invoice()
        res["salesperson_id"] = self.salesperson_id.id
        return res

    def action_view_invoice(self):
        res = super().action_view_invoice()
        if len(self) == 1:
            res["context"]["default_salesperson_id"] = self.salesperson_id.id
        return res


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    salesman_id = fields.Many2one(
        string="Salesperson (not used)",
    )
    salesperson_id = fields.Many2one(
        related="order_id.salesperson_id",
        string="Salesperson",
        store=True,
        readonly=True,
        index=True,
    )
