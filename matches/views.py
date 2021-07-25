from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Club, Fee, Team, Game, Chat
from checkout.models import Order
from profiles.models import UserProfile
from .forms import GameForm, CompetitionForm, ChatForm, FeesForm, ClubForm, TeamForm

import json
import datetime


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
            q1 = request.GET['age']
            q2 = request.GET['team']
            qu1 = Q(home_team__team_name__contains=q1) | Q(
                    away_team__team_name__contains=q1)
            qu2 = Q(home_team__team_name=q2) | Q(away_team__team_name=q2)
            matches = matches.filter(qu1, qu2)

        if 'team' in request.GET:
            team = request.GET['team']
            if not team:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('matches'))
            query2 = Q(home_team__team_name=team) | Q(
                    away_team__team_name=team)
            matches = matches.filter(query2)

        if 'age' in request.GET:
            age_group = request.GET['age']
            if not age_group:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('matches'))            
            query1 = Q(home_team__team_name__contains=age_group) | Q(
                 away_team__team_name__contains=age_group)
            matches = matches.filter(query1)
        
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
    name = user.get_full_name
    job = False

    profile = UserProfile.objects.get(user=user)
    role = profile.role

    match = get_object_or_404(Game, pk=game_id)
    ref = str(match.referee)
    coach = match.home_team.manager_coach

    # Determine User Role
    if role == "Coach" or role == "Referee":
        job = True

    # Calculate and save Match officials fees
    if match.referee is None:
        ref_total = 0
    else:
        ref_fee = match.home_team.age.referee_fee
        ref_trav = match.ref_trav
        ref_total = ref_fee + ref_trav
        match.ref_total = ref_total

    if match.asst_referee1 is None:
        asst1_total = 0
    else:
        asst1_fee = match.home_team.age.asst_referee
        asst1_trav = match.asst1_trav
        asst1_total = asst1_fee + asst1_trav
        match.asst1_total = asst1_total

    if match.asst_referee2 is None:
        asst2_total = 0
    else:
        asst2_fee = match.home_team.age.asst_referee
        asst2_trav = match.asst2_trav
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

    # Determine whether the match is in the future or past
    # Only allow messages if in the future
    post = False
    today = datetime.datetime.now()
    if match.date_time.replace(tzinfo=None) > today:
        post = True

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
        'ref': ref,
        'orders': orders,
        'paid': paid,
        'post': post,
        'job': job,
        'coach': coach,
        'name': name,
    }

    return render(request, 'matches/match_detail.html', context)


@login_required
def add_travel(request, game_id):
    """
    Allows Match officials to update their travel expenses
    """
    match = get_object_or_404(Game, pk=game_id)
    user = request.user
    ref = str(match.referee)
    asst1 = str(match.asst_referee1)
    asst2 = str(match.asst_referee2)

    if request.method == 'POST':
        form = FeesForm(request.POST, instance=match)
        if form.is_valid:
            form.save()
            messages.success(request, 'You successfully updated your travel \
                             expenses!')
            return redirect(reverse('match_detail', args=[match.id]))
        else:
            messages.error(request, "Failed to update your expenses\
                Please ensure the form is valis.")

    else:
        form = FeesForm(instance=match)

    template = 'matches/add_travel.html'
    context = {
        'form': form,
        'user': user,
        'ref': ref,
        'asst1': asst1,
        'asst2': asst2,
        'match': match,
    }

    return render(request, template, context)


@login_required
def add_competition(request):
    """ Add a new competition to the app """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have the permissions to \
                       add a competition!")
        return redirect(reverse, 'home')

    if request.method == "POST":
        form = CompetitionForm(request.POST)
        if form.is_valid():
            competition = form.save()
            messages.success(request, 'You successfully added a new \
                             competition!')
            return redirect(reverse('matches'))
        else:
            messages.error(request, 'Failed to create a new competition. \
                Please ensure the form has valid inputs')
    else:
        form = CompetitionForm()

    template = 'matches/add_competition.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_club(request):
    """ Add a new Club to the DB """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have the permissions to \
                       add a club!")
        return redirect(reverse, 'home')

    if request.method == "POST":
        form = ClubForm(request.POST, request.FILES)
        if form.is_valid:
            club = form.save()
            messages.success(request, 'You successfully added a new club!')
            return redirect(reverse('matches'))
        else:
            messages.error(request, 'Failed to create a new club. \
                Please ensure the form has valid inputs')
    else:
        form = ClubForm()

    template = 'matches/add_club.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_team(request):
    """ Add a new Team to the DB """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have the permissions to \
                       add a team!")
        return redirect(reverse, 'home')

    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid:
            team = form.save()
            messages.success(request, 'You successfully added a new team!')
            return redirect(reverse('matches'))
        else:
            messages.error(request, 'Failed to create a new team. \
                Please ensure the form has valid inputs')
    else:
        form = TeamForm()

    template = 'matches/add_team.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_match(request):
    """ Add a new game to the app """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have the permissions to \
                       add a match!")
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
        messages.error(request, "Sorry, you don't have the permissions to \
                       edit a match!")
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
    chats = Chat.objects.all()
    ref = str(match.referee)

    context = {
        'match': match,
        'chats': chats,
        'ref': ref,
    }

    return render(request, 'matches/match_chat.html', context)


@login_required
def add_chat(request, game_id):
    match = get_object_or_404(Game, pk=game_id)
    user = request.user
    data = {
        'match': match,
        'author': user,
        }
    if request.method == "POST":
        form = ChatForm(request.POST, request.FILES)
        if form.is_valid:
            chat = form.save()
            messages.success(request, 'You successfully added a new message!')
            return redirect(reverse('match_chat', args=[match.id]))
        else:
            messages.error(request, 'Failed to create a new message. \
                Please ensure the form has valid inputs')
    else:
        form = ChatForm(initial=data)

    template = 'matches/add_chat.html'
    context = {
        'form': form,
        'match': match,
        'author': user,
    }

    return render(request, template, context)
