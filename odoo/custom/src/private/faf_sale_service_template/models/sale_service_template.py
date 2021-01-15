# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class SaleServiceTemplate(models.Model):
    _name = "sale.service.template"
    _description = "Sale Service Template"

    name = fields.Char(required=True)
    description = fields.Html()
    active = fields.Boolean(default=True)
    type = fields.Selection(
        selection=[
            ("include", "Service Include"),
            ("exclude", "Service Exclude"),
        ]
    )
