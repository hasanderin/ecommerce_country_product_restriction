odoo.define('ecommerce_country_product_restriction.disable_button', function(require) {
    'use strict';
    $(document).ready(function() {
        setTimeout(function(e) {
            if ($("#div_pay").length) {
                $("button[name='o_payment_submit_button']").attr('disabled', 'disable');
                $("div[name='o_payment_option_card']").css({'opacity': '0.65' ,'pointer-events': 'none'})
            }
        }, 200)
    });
});
