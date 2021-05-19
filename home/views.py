from django.shortcuts import render

# Create your views here.


def index(request):
    """ This view will render the home page """

    return render(request, 'home/index.html')
