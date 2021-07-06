from django.shortcuts import get_object_or_404
from django.conf import settings
from matches.models import Game

import datetime

def bag_contents(request):

    bag_items = []    
    match_total = 0
    match_sub_total = 0
    grand_total = 0
    match_count = 0
    match_fines = 0    

    bag = request.session.get('bag', {})      

    for item_id, quantity in bag.items():
        match = get_object_or_404(Game, pk=item_id)
        match_sub_total = match.ref_total + match.asst1_total + match.asst2_total
        payment_due_date = match.date_time + datetime.timedelta(days=1)
        today = datetime.datetime.now()        
        if today > payment_due_date.replace(tzinfo=None):
            match_fines = settings.NONPAYMENT_FINE
        else:
            match_fines = 0
        match_total = match_sub_total + match_fines
        match_count += quantity
        grand_total += match_total

        bag_items.append({
            'item_id': item_id,
            'grand_total': grand_total,
            'match_total': match_total,
            'match': match,
            'quantity': quantity,
            'match_fines': match_fines,
            'payment_due_date': payment_due_date,
            'match_sub_total': match_sub_total,
        })

    context = {        
        'bag_items': bag_items,
        'match_total': match_total,
        'grand_total': grand_total,
        'match_count': match_count,
        'match_sub_total': match_sub_total,        
        'match_fines': match_fines,    
    }

    return context
