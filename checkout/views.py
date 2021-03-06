from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .forms import OrderForm
from .models import Order, OrderLineItem
from matches.models import Game
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from bag.contexts import bag_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """ A view to cache checkout data when the
    Checkout form is submitted
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


@login_required
def checkout(request):
    """  A view to render information on the Checkout Page """
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
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_qty in bag.items():
                try:
                    match = Game.objects.get(id=item_id)
                    if isinstance(item_qty, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            match=match,
                        )
                        order_line_item.save()
                except Game.DoesNotExist:
                    messages.error(request, (
                        "One of the matches in your kit bag wasn't found \
                            in our database."
                        "Please contact us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('review_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number])
            )
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

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.profile_phone_number,
                    'street_address1': profile.profile_street_address1,
                    'street_address2': profile.profile_street_address2,
                    'town_or_city': profile.profile_town_or_city,
                    'county_or_state': profile.profile_county,
                    'country': profile.profile_country,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
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


@login_required
def checkout_success(request, order_number):
    """ A view for successful transactions """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    short_order = order_number[0:11]
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach user profile to order
        order.user_profile = profile
        order.save()

        # Save the user info
        if save_info:
            profile_data = {
                'profile_phone_number': order.phone_number,
                'profile_street_address1': order.street_address1,
                'profile_street_address2': order.street_address2,
                'profile_town_or_city': order.town_or_city,
                'profile_county': order.county_or_state,
                'profile_postcode': order.postcode,
                'profile_country': order.country,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order succesfully processed! \
        Your transaction number is {short_order}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'short_order': short_order,
    }

    return render(request, template, context)
