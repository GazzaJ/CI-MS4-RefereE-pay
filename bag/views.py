from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def review_bag(request):
    """ This view will render the contents of our bag
    e.g. the matches we are trying to pay for
    """
    
    return render(request, 'bag/bag.html')


@login_required
def add_to_bag(request, item_id):
    """ Add the match fees to the shopping bag """    

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')    

    # Check if bag in session, create one if not
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        messages.error(request, 'This item is already in your bag')
    else:
        # Add the Product ID and Quantity to the bag
        bag[item_id] = quantity

    request.session['bag'] = bag    
    return redirect(redirect_url)
