# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    company_bank_id = fields.Many2one(
        comodel_name="res.partner.bank",
        string="Company Bank Account",
        config_parameter="sale.company_bank_id",
        ondelete="restrict",
        index=True,
    )
