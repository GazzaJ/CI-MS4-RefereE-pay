from django.http import HttpResponse


class StripeWH_Handler:
    """ Manages Stripe Webhooks """

    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
        """
        Deal with a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received:{event[type]}',
            status=200)
