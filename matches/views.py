from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
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

    query1 = None
    
    if request.GET:
        if 'age' in request.GET:
            age_group = request.GET['age']
            print(age_group)
            query1 = Q(age__age=age_group) | Q(age__age=age_group)
            matches = matches.filter(query1)

        if 'team' in request.GET:
            team = request.GET['team']            
            query2 = Q(home_team__team_name=team) | Q(away_team__team_name=team)
            matches = matches.filter(query2)        

        else:
            messages.error(request, "You didn't enter any search criteria")
            return redirect(reverse('matches'))

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

    ref_fee = 0
    ref_trav = 0
    ref_total = 0
    asst1_fee = 0
    asst1_trav = 0
    asst1_total = 0
    asst2_fee = 0
    asst2_trav = 0
    asst2_total = 0

    match = get_object_or_404(Game, pk=game_id)
    if match.referee is None:
        ref_total = 0
    else:
        ref_fee = match.home_team.age.referee_fee
        ref_trav = 0
        ref_total = ref_fee + ref_trav
        match.ref_total = ref_total

    if match.asst_referee1 is None:
        asst1_total = 0
    else:
        asst1_fee = match.home_team.age.asst_referee
        asst1_trav = 0
        asst1_total = asst1_fee + asst1_trav
        match.asst1_total = asst1_total

    if match.asst_referee2 is None:
        asst2_total = 0
    else:
        asst2_fee = match.home_team.age.asst_referee
        asst2_trav = 0
        asst2_total = asst2_fee + asst2_trav
        match.asst2_total = asst2_total

    match.save()

    context = {
        'match': match,
        'ref_fee': ref_fee,
        'ref_trav': ref_trav,
        'ref_total': ref_total,
        'asst1_fee': asst1_fee,
        'asst1_trav': asst1_trav,
        'asst1_total': asst1_total,
        'asst2_fee': asst2_fee,
        'asst2_trav': asst2_trav,
        'asst2_total': asst2_total
    }

    return render(request, 'matches/match_detail.html', context)

