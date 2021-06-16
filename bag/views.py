from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from decimal import Decimal


def review_bag(request):
    """ This view will render the contents of our bag
    e.g. the matches we are trying to pay for
    """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add the match fees to the shopping bag """

    ref = request.POST.get('ref')
    asst1 = request.POST.get('asst1')
    asst2 = request.POST.get('asst2')
    redirect_url = request.POST.get('redirect_url')

    # Check if bag in session, create one if not
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        messages.error(request, 'This item is already in your bag')
    else:
        # Add the Product ID and Quantity to the bag
        bag[item_id] = ref, asst1, asst2

    request.session['bag'] = bag
    print(request.session['bag'])    
    return redirect(redirect_url)
