/*  
    Core logic and payment flow come from
    https://stripe.com/docs/payments/accept-a-payment
*/

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key)
var elements = stripe.elements();
var style = {
    base: {
        color: '#303238',
        fontSize: '16px',
        fontFamily: '"Roboto", sans-serif',
        fontSmoothing: 'antialiased',
        '::placeholder': {
            color: '#CFD7DF',
        },
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    },
};

var card = elements.create('card',{style: style});
card.mount('#card-element');