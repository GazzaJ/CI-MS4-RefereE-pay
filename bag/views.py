from django.shortcuts import render


def review_bag(request):
    """ This view will render the contents of our bag
    e.g. the matches we are trying to pay for
    """

    return render(request, 'bag/bag.html')