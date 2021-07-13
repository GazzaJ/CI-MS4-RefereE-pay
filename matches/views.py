from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Club, Fee, Team, Game
from checkout.models import Order
from .forms import GameForm, CompetitionForm

import json


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

    user = request.user
    
    # Calculate and save Match officials fees
    
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

    # Determine whether a fixture has been paid for or not
    paid = False
    orders = Order.objects.all()
    for order in orders:        
        bag = order.original_bag
        new_bag = json.loads(bag)

        if game_id in new_bag.keys():
            paid = True

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
        'asst2_total': asst2_total,
        'user': user,
        'orders': orders,
        'paid': paid,

    }

    return render(request, 'matches/match_detail.html', context)


def add_competition(request):
    """ Add a new competition to the app """
    if request.method == "POST":
        comp_form = CompetitionForm(request.POST)
        if comp_form.is_valid():
            messages.success(request, 'You successfully added a new competition!')
            return redirect(request, 'add_match')
        else:
            messages.error(request, 'Failed to create a new competition. \
                Please ensure the form has valid inputs')
    else:
        comp_form = CompetitionForm()

    template = 'matches/add_match.html'
    context = {
        'comp_form': comp_form,
    }

    return render(request, template, context)


def add_match(request):
    """ Add a new game to the app """
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid:
            match = form.save()
            messages.success(request, 'You successfully added a new match!')
            return redirect(reverse('match_detail', args=[match.id]))
        else:
            messages.error(request, 'Failed to create a new match. \
                Please ensure the form has valid inputs')
    else:
        form = GameForm()

    template = 'matches/add_match.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_match(request, game_id):
    """ Edit the selected match details """
    match = get_object_or_404(Game, pk=game_id)
    if request.method == "POST":
        form = GameForm(request.POST, instance=match)
        if form.is_valid:
            form.save()
            messages.success(request, 'You successfully updated the match!')
            return redirect(reverse('match_detail', args=[match.id]))
        else:
            messages.error(request, 'Failed to update the match. \
                Please ensure the form has valid inputs')
    else:
        form = GameForm(instance=match)
        messages.info(request, f'You are editting {match.home_team} vs {match.away_team}')

    template = 'matches/edit_match.html'
    context = {
        'form': form,
        'match': match,
    }

    return render(request, template, context)


def delete_match(request, game_id):
    """ Deletes the selected match details """
    match = get_object_or_404(Game, pk=game_id)
    match.delete()
    messages.success(request, 'You have successfully deleted the match!')
    return redirect(reverse('matches'))
