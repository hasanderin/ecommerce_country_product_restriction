# -*- coding: utf-8 -*-
# Part of Odoo, Aktiv Software PVT. LTD.
# See LICENSE file for full copyright & licensing details.

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    country_ids = fields.Many2many(
        "res.country",
        "res_country_product_template_rel",
        string="Selected Countries",
        help="This Product is available for selected countries. If none is selected it is available for all countries.",
    )
