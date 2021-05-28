from django.shortcuts import render
from .models import Venue, Club, Age_Group, Fee, Team, Game


def all_matches(request):
    """
    This view will render the matches
    including, sorting and searching
    """

    matches = Game.object.all()

    context = {
        'matches': matches,
    }

    return render(request, 'matches/matches.html', context)
