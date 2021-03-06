""" Test views file for unit testing of Matches app views """
from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse


class TestMatchesViews(TestCase):
    """ Testcases for matches app views """
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            'admin', 'admin@email.com', 'adminpass')
        self.matches = reverse("matches")

    def test_get_fixture_list_view(self):
        """ Tests the Matches (fixture list) view """

        response = self.client.get('/matches/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'matches/matches.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_club_directory_view(self):
        """ Tests the Clubs view """

        response = self.client.get('/matches/clubs')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'matches/clubs.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_get_add_competition(self):
        """ Tests the Add Competition view """

        self.client.login(
            username='admin',
            password='adminpass'
            )

        response = self.client.get('/matches/comp/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'matches/add_competition.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_get_add_club(self):
        """ Tests the Add Club view """

        self.client.login(
            username='admin',
            password='adminpass'
            )

        response = self.client.get('/matches/club/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'matches/add_club.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_get_add_team(self):
        """ Tests the Add Team View """

        self.client.login(
            username='admin',
            password='adminpass'
            )

        response = self.client.get('/matches/team/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'matches/add_team.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_get_add_match(self):
        """ Tests the Add Match view """

        self.client.login(
            username='admin',
            password='adminpass'
            )

        response = self.client.get('/matches/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'matches/add_match.html')
        self.assertTemplateUsed(response, 'base.html')
