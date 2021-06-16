from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from decimal import Decimal

from .models import Venue, Club, Fee, Team, Game


def all_matches(request):
    """
    This view will render the matches
    including, sorting and searching
    """

    matches = Game.objects.all()    
    teams = Team.objects.all()
    clubs = Club.objects.all()
    fees = Fee.objects.all()    

    context = {
        'matches': matches,
        'teams': teams,
        'clubs': clubs,
        'fees': fees,
    }

    return render(request, 'matches/matches.html', context)


@login_required
def match_detail(request, game_id):
    """
    This view will render the full details
    of each individual match when selected
    """

    match = get_object_or_404(Game, pk=game_id)
    ref_fee = Decimal(match.home_team.age.referee_fee)
    asst1_fee = Decimal(match.home_team.age.asst_referee)
    asst2_fee = Decimal(match.home_team.age.asst_referee)

    context = {
        'match': match,
        'ref_fee': ref_fee,
        'asst1_fee': asst1_fee,
        'asst2_fee': asst2_fee,
    }

    return render(request, 'matches/match_detail.html', context)


@login_required
def match_fees(request, game_id):
    """
    This view will render the full details
    of each individual match when selected
    """

    match = get_object_or_404(Game, pk=game_id)    

    context = {
        'match': match        
    }

    return render(request, 'matches/match_fees.html', context)
