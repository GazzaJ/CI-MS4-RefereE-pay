from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404


def review_bag(request):
    """ This view will render the contents of our bag
    e.g. the matches we are trying to pay for
    """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add the match fees to the shopping bag """
    quantity = int(request.POST.get('ref-fee'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
