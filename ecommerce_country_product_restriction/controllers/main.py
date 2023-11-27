# -*- coding: utf-8 -*-
# Part of Odoo, Aktiv Software PVT. LTD.
# See LICENSE file for full copyright & licensing details.

from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSale(WebsiteSale):
    @http.route()
    def address(self, **kw):
        rec = super(WebsiteSale, self).address(**kw)
        if request.website.country_ids:
            rec.qcontext.update({"countries": request.website.country_ids})
        return rec

    @http.route(
        ["/shop/checkout"], type="http", auth="public", website=True, sitemap=False
    )
    def checkout(self, **post):
        rec = super(WebsiteSale, self).checkout(**post)
        order = request.website.sale_get_order()
        product_not_available = False
        if order.partner_shipping_id and order.partner_shipping_id.country_id:
            for line in order.order_line:
                if (
                    line.product_id.country_ids
                    and order.partner_shipping_id.country_id.id
                    not in line.product_id.country_ids.ids
                ):
                    product_not_available = True
        if rec.qcontext.get("shippings") and len(rec.qcontext.get("shippings")) == 1:
            rec.qcontext.update({"one_shipping": True})
        rec.qcontext.update({"product_not_available": product_not_available})
        return rec

    @http.route(
        "/shop/payment", type="http", auth="public", website=True, sitemap=False
    )
    def shop_payment(self, **post):
        rec = super(WebsiteSale, self).shop_payment(**post)
        order = request.website.sale_get_order()
        product_not_available = False
        if order.partner_shipping_id and order.partner_shipping_id.country_id:
            for line in order.order_line:
                if (
                    line.product_id.country_ids
                    and order.partner_shipping_id.country_id.id
                    not in line.product_id.country_ids.ids
                ):
                    product_not_available = True
        rec.qcontext.update({"product_not_available": product_not_available})
        return rec
