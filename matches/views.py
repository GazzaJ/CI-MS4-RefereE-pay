from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Club, Fee, Team, Game
from checkout.models import Order
from .forms import GameForm, CompetitionForm, ChatForm

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
    query2 = None
    search = None

    if request.GET:
        if 'age' and 'team' in request.GET:
            print('BINGO!')
            q1 = request.GET['age']
            q2 = request.GET['team']
            qu1 = Q(home_team__team_name__contains=q1) | Q(
                    away_team__team_name__contains=q1)
            qu2 = Q(home_team__team_name=q2) | Q(away_team__team_name=q2)
            matches = matches.filter(qu1, qu2)

        if 'team' in request.GET:
            team = request.GET['team']
            query2 = Q(home_team__team_name=team) | Q(
                       away_team__team_name=team)
            matches = matches.filter(query2)

        elif 'age' in request.GET:
            age_group = request.GET['age']            
            query1 = Q(home_team__team_name__contains=age_group) | Q(
                       away_team__team_name__contains=age_group)
            matches = matches.filter(query1)

        else:
            messages.error(request, "You didn't enter any search criteria")
            return redirect(reverse('matches'))

        # Filter results by search box query
        if 'q' in request.GET:
            search = request.GET['q']
            if not search:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('matches'))
            searches = Q(home_team__team_name__icontains=search) | Q(
                away_team__team_name__icontains=search)
            matches = matches.filter(searches)

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


@login_required
def add_competition(request):
    """ Add a new competition to the app """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have the permissions to add a competition!")
        return redirect(reverse, 'home')

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


@login_required
def add_match(request):
    """ Add a new game to the app """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have the permissions to add a amtch!")
        return redirect(reverse, 'home')

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


@login_required
def edit_match(request, game_id):
    """ Edit the selected match details """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have the permissions to edit a match!")
        return redirect(reverse, 'home')

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


@login_required
def delete_match(request, game_id):
    """ Deletes the selected match details """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have the permissions to delete a match!")
        return redirect(reverse, 'home')

    match = get_object_or_404(Game, pk=game_id)
    match.delete()
    messages.success(request, 'You have successfully deleted the match!')
    return redirect(reverse('matches'))


@login_required
def match_chat(request, game_id):
    match = get_object_or_404(Game, pk=game_id)

    context = {
        'match': match,
    }

    return render(request, 'matches/match_chat.html', context)


@login_required
def add_chat(request, game_id):
    match = get_object_or_404(Game, pk=game_id)
    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid:
            match = form.save()
            messages.success(request, 'You successfully added a new message!')
            return redirect(reverse('match_chat', args=[match.id]))
        else:
            messages.error(request, 'Failed to create a new message. \
                Please ensure the form has valid inputs')
    else:
        form = ChatForm()

    template = 'matches/add_chat.html'
    context = {
        'form': form,
        'match': match,
    }

    return render(request, template, context)
