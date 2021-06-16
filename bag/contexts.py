from django.shortcuts import get_object_or_404
from matches.models import Game

def bag_contents(request):
    
    bag_items = []
    ref_total = 0
    asst1_total = 0
    asst2_total = 0
    match_count = 0
    grand_total = 0
    bag = request.session.get('bag', {})    

    #for item, quantity in bag.items():
    #    match = get_object_or_404(Match, pk=item_id)
    #    if match.referee:
    #        ref_id =             
    #        ref_fee = match.ref_fee
    #        if ref_trav:
    #            ref_total = ref_fee + ref_trav
    #        else:
    #            ref_total = ref_fee
#
    #    if match.asst_referee1:
    #        asst1_fee = match.asst1_fee
    #    if match.asst_referee2:
    #        asst2_fee = match.asst2_fee

    #    grand_total  = ref_total + asst1_total + asst2_total
    #    bag_items.append({
    #        'item_id': item_id,
    #        'quantity': quantity,
    #        'match': match
    #    })

    context = {
        'bag_items': bag_items,
        'ref_total': ref_total,
        'match_count': match_count,
        'grand_total': grand_total,
    }

    return context
