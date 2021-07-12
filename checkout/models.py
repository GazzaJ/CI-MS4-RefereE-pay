import uuid

from django.db import models
from django_countries.fields import CountryField
from django.db.models import Sum
from django.conf import settings
import datetime

from matches.models import Game
from profiles.models import UserProfile


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, null=True, blank=True,
                                     related_name="orders", 
                                     on_delete=models.SET_NULL)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county_or_state = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=True, blank=True)    
    date = models.DateTimeField(auto_now_add=True)
    grand_total = models.DecimalField(max_digits=6, decimal_places=2,
                                      null=False, default=0)
    original_bag = models.CharField(max_length=200, null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """ Generate a unique order number using UUID """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total anytime a linitem is added
        """
        self.grand_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
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


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    match = models.ForeignKey(Game, null=False, blank=False, on_delete=models.CASCADE)
    payment_due_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    match_fees = models.DecimalField(max_digits=6, decimal_places=2,
                                      null=False, default=0)
    match_fines = models.DecimalField(max_digits=6, decimal_places=2,
                                      null=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem
        total and update the grand total
        """        
        if self.payment_due_date is None:
            self.payment_due_date = self.match.date_time + datetime.timedelta(days=1)
            if self.order.date > self.payment_due_date:
                self.match_fines = settings.NONPAYMENT_FINE
            else:
                self.match_fines = 0
        self.match_fees = self.match.ref_total + self.match.asst1_total + self.match.asst2_total
        self.lineitem_total = self.match.ref_total + self.match.asst1_total + self.match.asst2_total + self.match_fines
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Match Total {self.lineitem_total} on {self.order.order_number}'
