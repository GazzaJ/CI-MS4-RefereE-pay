from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField


class Venue(models.Model):
    name = models.CharField(max_length=254, null=True, blank=False)
    short_name = models.CharField(max_length=100, null=False, blank=False)
    street_address = models.CharField(max_length=80, null=False, blank=False)
    town_or_city = models.CharField(max_length=50, null=False, blank=False)
    county = models.CharField(max_length=60, null=False, blank=False)
    postcode = models.CharField(max_length=50, null=False, blank=False)
    country = CountryField(blank_label='Country', null=True, blank=True)
    map = models.ImageField(null=True, blank=True)
    map_url = models.URLField(max_length=1024, null=False, blank=False)

    def __str__(self):
        return self.name

    def get_short_name(self):
        return self.short_name


class Official(models.Model):
    name = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.name


class Competition(models.Model):
    comp = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.comp


class Club(models.Model):
    club_name = models.CharField(max_length=254, null=False, blank=False)
    club_badge_url = models.URLField(max_length=1024, null=False, blank=False)
    club_badge = models.ImageField(null=True, blank=True)
    website_url = models.URLField(max_length=1024, null=False, blank=False)

    def __str__(self):
        return self.club_name

    class Meta:
        ordering = ['club_name']


class Fee(models.Model):
    age = models.CharField(max_length=50, null=True, blank=False)
    referee_fee = models.DecimalField(max_digits=6, decimal_places=2,
                                      null=False, default=0)
    asst_referee = models.DecimalField(max_digits=6, decimal_places=2,
                                       null=False, default=0)
    milage_rate = models.DecimalField(max_digits=6, decimal_places=2,
                                      null=False, default=0)

    def __str__(self):
        return str(self.age)


class Team(models.Model):
    team_name = models.CharField(max_length=100, null=False, blank=False)
    short_name = models.CharField(max_length=100, null=False, blank=False)
    club_name = models.ForeignKey('Club', null=False, blank=False,
                                  on_delete=models.CASCADE)
    age = models.ForeignKey('Fee', null=True, blank=False,
                            on_delete=models.CASCADE)
    manager_coach = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.team_name


class Game(models.Model):
    age = models.ForeignKey('Fee', null=True, blank=False,
                            related_name="age_group", on_delete=models.CASCADE)
    competition = models.ForeignKey('Competition', null=False, blank=False,
                                    on_delete=models.CASCADE)     
    home_team = models.ForeignKey('Team', related_name='home_team', null=False,
                                  blank=False, on_delete=models.CASCADE)
    away_team = models.ForeignKey('Team', related_name='away_team', null=False,
                                  blank=False, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)    
    venue = models.ForeignKey('Venue', null=True, blank=False,
                              on_delete=models.SET_NULL)
    referee = models.ForeignKey('Official', related_name='ref', null=True,
                                blank=True, on_delete=models.SET_NULL)
    asst_referee1 = models.ForeignKey('Official', related_name='asst1',
                                      null=True, blank=True,
                                      on_delete=models.SET_NULL)
    asst_referee2 = models.ForeignKey('Official', related_name='asst2',
                                      null=True, blank=True,
                                      on_delete=models.SET_NULL)
    ref_trav = models.DecimalField(max_digits=6, decimal_places=2, blank=True,
                                   null=True, default=0)
    asst1_trav = models.DecimalField(max_digits=6, decimal_places=2, 
                                     blank=True, null=True, default=0)
    asst2_trav = models.DecimalField(max_digits=6, decimal_places=2, 
                                     blank=True, null=True, default=0)
    ref_total = models.DecimalField(max_digits=6, decimal_places=2,
                                    null=False, default=0)
    asst1_total = models.DecimalField(max_digits=6, decimal_places=2,
                                      null=False, default=0)
    asst2_total = models.DecimalField(max_digits=6, decimal_places=2,
                                      null=False, default=0)

    def __str__(self):
        return f'{self.home_team} vs {self.away_team}'

    class Meta:
        ordering = ['date_time']


class Chat(models.Model):
    match = models.ForeignKey(Game, null=False, blank=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User, max_length=100, blank=False, null=False, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.body
