from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order
from matches.models import Game
from bag.contexts import bag_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county_or_state': request.POST['county_or_state'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_qty in bag.items():
                try:
                    match = Game.objects.get(id=item_id)
                    # my code
                    ref_total = match.ref_total
                    asst1_total = match.asst1_total
                    asst2_total = match.asst2_total
                    match_fines = 0
                    off_total = ref_total + asst1_total + asst2_total
                    match_total = off_total + match_fines
                    # end of my code
                    order.save()
                except Game.DoesNotExist:
                    messages.error(request, (
                        "One of the matches in your kit bag wasn't found \
                            in our database."
                        "Please contact us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('review_bag'))

            request.session['save-info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There is nothing in your kit \
                bag at the moment")
            return redirect(reverse('matches'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']        
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing! \
            Did you forget to set it in the environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """ A view for successful transactions """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order succesfully processed! \
        Your transaction number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
