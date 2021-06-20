from decimal import Decimal
from django.shortcuts import get_object_or_404
from matches.models import Game


def bag_contents(request):

    bag_items = []
    grand_total = 0

    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        match = get_object_or_404(Game, pk=item_id)

        bag_items.append({
            'item_id': item_id,
            'grand_total': grand_total,
            'match': match,
            'quantity': quantity,
        })   

    context = {        
        'bag_items': bag_items,
        'grand_total': grand_total,
    }

    return context
