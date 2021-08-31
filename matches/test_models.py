from django.test import TestCase
from .models import Fee, Venue, Official, Competition, Club


class TestModels(TestCase):

    def test_venue_string_method_returns_name(self):
        """ Test venue string method """
        venue = Venue.objects.create(name='Wembley Stadium')
        self.assertEqual(str(venue), 'Wembley Stadium')

    def test_venue_string_method_returns_short_name(self):
        """ Test short name string method """
        short = Venue.objects.create(short_name='Wembley')
        self.assertTrue(short, 'Wembley')

    def test_official_string_method_returns_name(self):
        """ Test match official string method """
        official = Official.objects.create(name='John Smith')
        self.assertEqual(str(official), 'John Smith')

    def test_competition_string_method_returns_name(self):
        """ Test competition string method """
        competition = Competition.objects.create(comp='Wembley Stadium')
        self.assertEqual(str(competition), 'Wembley Stadium')

    def test_club_string_method_returns_name(self):
        """ Test club name string method """
        club = Club.objects.create(club_name='Nottingham Forest')
        self.assertEqual(str(club), 'Nottingham Forest')

    def test_fee_string_method_returns_age(self):
        """ Test fee string method """
        fee = Fee.objects.create(age='U50')
        self.assertEqual(str(fee), 'U50')
