# Copyright 2021 Ecosoft Co., Ltd (http://ecosoft.co.th)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models


class AccountPayment(models.Model):
    _inherit = "account.payment"

    salesperson_id = fields.Many2one(
        comodel_name="hr.employee",
        domain=lambda self: self._get_domain_salesperson_id(),
        ondelete="restrict",
        index=True,
    )

    @api.model
    def default_get(self, default_fields):
        res = super().default_get(default_fields)
        context = self._context
        active_ids = context.get("active_ids")
        active_model = context.get("active_model")
        if not active_ids or active_model != "account.move":
            return res
        invoices = self.env[active_model].browse(active_ids)
        res.update(
            {
                "salesperson_id": invoices[0].salesperson_id.id,
            }
        )
        return res

    @api.model
    def _get_domain_salesperson_id(self):
        try:
            return [("department_id", "=", self.env.ref("hr.dep_sales").id)]
        except ValueError:
            return []


class AccountPaymentRegister(models.TransientModel):
    _inherit = "account.payment.register"

    salesperson_id = fields.Many2one(
        comodel_name="hr.employee",
        ondelete="set null",
        index=True,
    )

    def _create_payment_vals_from_wizard(self):
        vals = super()._create_payment_vals_from_wizard()
        vals["salesperson_id"] = self.salesperson_id.id
        return vals

    @api.model
    def _get_line_batch_key(self, line):
        vals = super()._get_line_batch_key(line)
        vals["salesperson_id"] = line.move_id.salesperson_id.id
        return vals

    @api.model
    def _get_wizard_values_from_batch(self, batch_result):
        vals = super()._get_wizard_values_from_batch(batch_result)
        vals["salesperson_id"] = batch_result["key_values"]["salesperson_id"]
        return vals

    def _create_payment_vals_from_batch(self, batch_result):
        vals = super()._create_payment_vals_from_batch(batch_result)
        batch_values = self._get_wizard_values_from_batch(batch_result)
        vals["salesperson_id"] = batch_values["salesperson_id"]
        return vals
