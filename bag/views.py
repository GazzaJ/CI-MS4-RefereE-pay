from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404


def review_bag(request):
    """ This view will render the contents of our bag
    e.g. the matches we are trying to pay for
    """

    return render(request, 'bag/bag.html')


def add_to_bag(request, match_id):
    """ Add the match fees tto the shopping bag """
