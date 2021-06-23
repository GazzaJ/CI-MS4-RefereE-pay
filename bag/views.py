from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from matches.models import Game


@login_required
def review_bag(request):
    """ This view will render the contents of our bag
    e.g. the matches we are trying to pay for
    """
    
    return render(request, 'bag/bag.html')


@login_required
def add_to_bag(request, item_id):
    """ Add the match fees to the shopping bag """    

    match = get_object_or_404(Game, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')    

    # Check if bag in session, create one if not
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        messages.error(request, 'This item is already in your bag')
    else:
        # Add the Product ID and Quantity to the bag
        bag[item_id] = quantity
        messages.success(request, f'Added {match.home_team} vs { match.away_team }to your kit bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


@login_required
def remove_from_bag(request, item_id):
    """ Removes the selected match from the kit bag """

    try:
        match = get_object_or_404(Game, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {match.home_team} vs {match.away_team} from your kit bag!')

        request.session['bag'] = bag
        return HttpResponse(status=200)               

    except Exception as e:
        messages.error(request, f'Error removing match {e}')
        return HttpResponse(status=500)
