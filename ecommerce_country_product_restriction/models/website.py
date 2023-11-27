# -*- coding: utf-8 -*-
# Part of Odoo, Aktiv Software PVT. LTD.
# See LICENSE file for full copyright & licensing details.

from odoo import models, fields, _


class Website(models.Model):

    _inherit = "website"

    country_ids = fields.Many2many(
        "res.country", "res_country_website_rel", string="Selected Countries"
    )
    cart_message = fields.Char(
        string="Cart Message", default=_("Not available in your country.")
    )
    checkout_message = fields.Char(
        string="Checkout Message",
        default=_(
            "Some Products are not available for your country, please remove them from the cart to continue."
        ),
    )
