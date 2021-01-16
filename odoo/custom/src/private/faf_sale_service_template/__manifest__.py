# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "FAF - Sale Service Template",
    "summary": "Add sale service template",
    "version": "14.0.1.0.0",
    "category": "FAF",
    "website": "http://ecosoft.co.th",
    "author": "Tharathip C., Ecosoft",
    "depends": ["sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_config_settings_views.xml",
        "views/sale_views.xml",
        "views/sale_service_template_views.xml",
    ],
    "license": "AGPL-3",
    "installable": True,
    "maintainers": ["newtratip"],
}
