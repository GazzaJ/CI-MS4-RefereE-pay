from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Venue, Club, Fee, Team, Game


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


@login_required
def match_detail(request, game_id):
    """
    This view will render the full details
    of each individual match when selected
    """

    match = get_object_or_404(Game, pk=game_id)

    context = {
        'match': match
    }

    return render(request, 'matches/match_detail.html', context)
