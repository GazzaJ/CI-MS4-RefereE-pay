from django.shortcuts import render, get_object_or_404


def profile(request):
    """ Display the User Profile """
    
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
