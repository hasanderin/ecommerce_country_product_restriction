# -*- coding: utf-8 -*-
# Part of Odoo, Aktiv Software PVT. LTD.
# See LICENSE file for full copyright & licensing details.

# Author: Aktiv Software PVT. LTD.
# mail: odoo@aktivsoftware.com
# Copyright (C) 2015-Present Aktiv Software PVT. LTD.
# Contributions:
#   Aktiv Software:
#       - Burhan Vakharia
#       - Komal Jimudiya
#       - Tanvi Gajera
#       - Aarti Sathvara (Fix Issue)
{
    "name": "eCommerce Country Product Restriction",
    "summary": """
        With this module, users can restrict their product's availability for specific countries.
        eCommerce Country Product Restriction,
        Website Country Restriction,
        eCommerce Product Available by Country,
        Country Product Restriction,
        Country Product Restrict,
        Country Product Block,
        Product Block by country,
        Block Product by country,
        country block,
        Product Country Restriction,
        Country Restriction,
        Product Country Restrict,
        Product Restriction ,
        shopping cart,
        ecommerce website,
        ecommerce template,
        Product Restriction by country,
        odoo ecommerce,
        online store,
        ecommerce product,
        product ecommerce,
        product hide,
        hide product country,
        block user,
        block cart,
        restrict cart,
        filter country,
        filter product,
        product country,
        block product,
        stop product,
        disallow product,
        disallow cart,
        product availability,
        """,
    "description": """
        Title: POS Loyalty Management. \n
        Author: Aktiv Software PVT. LTD. \n
        mail: odoo@aktivsoftware.com \n
        Copyright (C) 2015-Present Aktiv Software PVt. LTD. \n
        Contributions: Aktiv Software:  \n
             - Burhan Vakharia
             - Komal Jimudiya
             - Tanvi Gajera
        With this module, users can restrict their product's availability for specific countries.
        For e.g., if product A is available in United States but is unavailable in Germany,  in such cases, this module will disable the payment option for the user wanting to buy the product A in Germany.
        eCommerce Country Product Restriction,
        Website Country Restriction,
        eCommerce Product Available by Country,
        Country Product Restriction,
        Country Product Restrict,
        Country Product Block,
        Product Block by country,
        Block Product by country,
        country block,
        Product Country Restriction,
        Country Restriction,
        Product Country Restrict,
        Product Restriction ,
        shopping cart,
        ecommerce website,
        ecommerce template,
        Product Restriction by country,
        odoo ecommerce,
        online store,
        ecommerce product,
        product ecommerce,
        product hide,
        hide product country,
        block user,
        block cart,
        restrict cart,
        filter country,
        filter product,
        product country,
        block product,
        stop product,
        disallow product,
        disallow cart,
        product availability,

    """,
    "author": "Aktiv Software Pvt Ltd",
    "website": "http://www.aktivsoftware.com",
    "category": "Website/Website",
    "version": "15.0.1.0.0",
    "license": "OPL-1",
    "price": 15.00,
    "currency": "EUR",
    "depends": ["website_sale"],
    "data": [
        "views/product_template_views.xml",
        "views/website_form_views.xml",
        "views/templates.xml",
    ],
    "images": ["static/description/banner.jpg"],
    "assets": {
        "web.assets_frontend": [
            "ecommerce_country_product_restriction/static/src/js/hover.js",
        ],
    },
}
