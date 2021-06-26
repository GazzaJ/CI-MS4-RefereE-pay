from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your kit bag at the moment")
        return redirect(reverse('matches'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51J6Y1QB2KPTgpLEAS9z7xZn7rBS2nwe1OJ1UvQzr9doMolVH2tgdgK5QsUXz8DJPy8YHuJK5FZvKS2dL5vodfcPj00l86IjwbJ'
    }

    return render(request, template, context)
