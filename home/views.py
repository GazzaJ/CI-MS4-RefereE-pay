from django.shortcuts import render


def index(request):
    """ This view will render the home page """

    return render(request, 'home/index.html')
