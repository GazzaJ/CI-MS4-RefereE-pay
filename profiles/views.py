from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    """ Display the User Profile """
    
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
