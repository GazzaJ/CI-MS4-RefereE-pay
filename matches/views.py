from django.shortcuts import render
from .models import Venue, Club, Age_Group, Fee, Team, Game


def all_matches(request):
    """
    This view will render the matches
    including, sorting and searching
    """

    matches = Game.objects.all()
    teams = Team.objects.all()
    clubs = Club.objects.all()

    context = {
        'matches': matches,
        'teams': teams,
        'clubs': clubs,
    }

    return render(request, 'matches/matches.html', context)
