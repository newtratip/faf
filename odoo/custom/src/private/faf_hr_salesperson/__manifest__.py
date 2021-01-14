# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "FAF - HR Salesperson",
    "summary": "Change salesperson from users to employees",
    "version": "14.0.1.0.0",
    "category": "FAF",
    "website": "http://ecosoft.co.th",
    "author": "Tharathip C., Ecosoft",
    "depends": ["account", "hr", "sale"],
    "data": [
        "report/account_invoice_report_views.xml",
        "report/sale_report_templates.xml",
        "report/sale_report_views.xml",
        "views/account_move_views.xml",
        "views/account_payment_views.xml",
        "views/res_partner_views.xml",
        "views/sale_views.xml",
    ],
    "license": "AGPL-3",
    "installable": True,
    "maintainers": ["newtratip"],
}
