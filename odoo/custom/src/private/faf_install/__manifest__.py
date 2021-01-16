# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "FAF - Install",
    "summary": "Listing of all required module for easy installation. "
    "**This module can be uninstalled afterwards**",
    "version": "14.0.1.0.0",
    "category": "FAF",
    "website": "http://ecosoft.co.th",
    "author": "Tharathip C., Ecosoft",
    "depends": [
        # OCA Modules
        "l10n_th_tax_invoice",
        # "l10n_th_tax_report",
        "l10n_th_withholding_tax",
        # "l10n_th_withholding_tax_cert",
        # "l10n_th_withholding_tax_cert_form",
        # "l10n_th_withholding_tax_report",
        # FAF Modules
        "faf_hr_salesperson",
        "faf_sale",
        "faf_sale_service_template",
    ],
    "license": "AGPL-3",
    "installable": True,
    "maintainers": ["newtratip"],
}
