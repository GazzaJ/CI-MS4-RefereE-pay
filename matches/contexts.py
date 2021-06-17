from django.shortcuts import get_object_or_404
from decimal import Decimal

from .models import Venue, Club, Fee, Team, Game


def match_details(request):

    game_total = 0
    ref_fee = 0
    ref_trav = 0
    ref_total = 0
    asst1_fee = 0
    asst1_trav = 0
    asst1_total = 0
    asst2_fee = 0
    asst2_trav = 0
    asst2_total = 0

    matches = Game.objects.all()
    for match in matches:        

        ref_fee = Decimal(match.home_team.age.referee_fee)
        ref_total = Decimal(ref_fee + ref_trav)

        asst1_fee = Decimal(match.home_team.age.asst_referee)
        asst1_total = Decimal(asst1_fee + asst1_trav)    

        asst2_fee = Decimal(match.home_team.age.asst_referee)
        asst2_total = Decimal(asst2_fee + asst2_trav)

    game_total = ref_total + asst1_total + asst2_total

    context = {
        'ref_fee': ref_fee,
        'ref_trav': ref_trav,
        'ref_total': ref_total,
        'asst1_fee': asst1_fee,
        'asst1_trav': asst1_trav,
        'asst1_total': asst1_total,
        'asst2_fee': asst2_fee,
        'asst2_trav': asst2_trav,
        'asst2_total': asst2_total,
        'game_total': game_total,
    }

    return context
