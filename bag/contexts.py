from django.shortcuts import get_object_or_404
from matches.models import Game


def bag_contents(request):

    bag_items = []    
    match_total = 0
    grand_total = 0
    match_count = 0

    bag = request.session.get('bag', {})      

    for item_id, quantity in bag.items():
        match = get_object_or_404(Game, pk=item_id)
        match_total = match.ref_total + match.asst1_total + match.asst2_total
        match_count += quantity
        grand_total += match_total

        bag_items.append({
            'item_id': item_id,
            'grand_total': grand_total,
            'match_total': match_total,
            'match': match,
            'quantity': quantity,
        })

    context = {        
        'bag_items': bag_items,
        'match_total': match_total,
        'grand_total': grand_total,
        'match_count': match_count,        
    }

    return context
