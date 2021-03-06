# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    # New fields
    relocation_from = fields.Char(
        string="Relocation From",
    )
    relocation_to = fields.Char(
        string="Relocation To",
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
    subject = fields.Char(
        string="Subject",
    )
