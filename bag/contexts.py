

def bag_contents(request):

    bag_items = []
    total = 0
    match_count = 0
    grand_total = 0

    context = {
        'bag_items': bag_items,
        'total': total,
        'match_count': match_count,
        'grand_total': grand_total,
    }

    return context
