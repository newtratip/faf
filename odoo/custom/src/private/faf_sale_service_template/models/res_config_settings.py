# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    service_include_id = fields.Many2one(
        comodel_name="sale.service.template",
        string="Service Include",
        domain="[('type', '=', 'include')]",
        config_parameter="sale.service_include_id",
        index=True,
    )
    service_exclude_id = fields.Many2one(
        comodel_name="sale.service.template",
        string="Service Exclude",
        domain="[('type', '=', 'exclude')]",
        config_parameter="sale.service_exclude_id",
        index=True,
    )
