import uuid

from django.db import models
from django_countries.fields import CountryField
from django.db.models import Sum

from matches.models import Game, Fee


class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county_or_state = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)    
    match_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    match_fines = models.ForeignKey(Fee, null=True, on_delete=models.SET_NULL, default=0)    
    grand_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """ Generate a unique order number using UUID """
        return uuid.uuid4().hex.upper()
    
    def update_total(self):
        """
        Update grand total each time a line item
        is added
        """
        self.match_total = ref_total + self.asst1_total + self.asst2_total
        # Add in fine for late payments here
        # something like if order_date > match_date
        # then lineitemtotal + fine
        self.grand_total = self.match_total+self.fines
        self.save()
    
    def save(self, *args, **kwargs):
        """
        Override the original save method to set an order number
        if it hasn't already been set
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number
