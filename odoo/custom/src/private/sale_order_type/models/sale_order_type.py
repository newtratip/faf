# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SaleOrderTypology(models.Model):
    _name = "sale.order.type"
    _description = "Type of sale order"

    @api.model
    def _get_domain_sequence_id(self):
        seq_type = self.env.ref("sale.seq_sale_order")
        return [("code", "=", seq_type.code)]

    name = fields.Char(required=True, translate=True)
    description = fields.Text(translate=True)
    sequence_id = fields.Many2one(
        comodel_name="ir.sequence",
        string="Entry Sequence",
        copy=False,
        domain=_get_domain_sequence_id,
    )
    journal_id = fields.Many2one(
        comodel_name="account.journal",
        string="Billing Journal",
        domain=[("type", "=", "sale")],
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        default=lambda self: self.env.user.company_id,
    )
    payment_term_id = fields.Many2one(
        comodel_name="account.payment.term", string="Payment Term"
    )
    pricelist_id = fields.Many2one(comodel_name="product.pricelist", string="Pricelist")
