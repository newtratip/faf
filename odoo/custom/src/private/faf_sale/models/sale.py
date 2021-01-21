# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    # New fields
    relocation = fields.Text(
        string="Relocation",
    )
    mode_shipment = fields.Text(
        string="Mode of Shipment",
    )
    not_exceeding_estimated_volume = fields.Text(
        string="Not exceeding the estimated volume of",
    )
    first_day_packing = fields.Char(
        string="First Day of Packing",
    )
    last_day_packing = fields.Char(
        string="Last Day of Packing",
    )
    transit_time = fields.Char(
        string="Port to Port Transit Time",
    )
    customs_clearlance = fields.Char(
        string="Customs Clearlance",
    )
    company_bank_id = fields.Many2one(
        comodel_name="res.partner.bank",
        string="Company Bank Account",
        compute="_compute_company_bank_id",
    )
    subject = fields.Char(
        string="Subject",
    )

    def _compute_company_bank_id(self):
        Bank = self.env["res.partner.bank"]
        for rec in self:
            company_bank_id = (
                self.env["ir.config_parameter"].sudo().get_param("sale.company_bank_id")
            )
            bank = Bank.search([("id", "=", int(company_bank_id))])
            rec.company_bank_id = bank.id
