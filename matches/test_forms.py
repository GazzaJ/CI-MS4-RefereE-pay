from django.test import TestCase
from .forms import FeesForm, CompetitionForm, ClubForm, TeamForm, GameForm, ChatForm


class TestFeesForm(TestCase):

    def test_age_field_not_required(self):
        form = FeesForm({'age': 'U12'})
        self.assertTrue(form.is_valid())

    def test_ref_trav_not_required(self):
        form = FeesForm({'ref_trav': '5'})
        self.assertTrue(form.is_valid())

    def test_asst1_trav_not_required(self):
        form = FeesForm({'asst1_trav': '6'})
        self.assertTrue(form.is_valid())

    def test_asst2_trav_not_required(self):
        form = FeesForm({'asst2_trav': '7'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = FeesForm()
        self.assertEqual(form.Meta.fields, ('ref_trav', 'asst1_trav', 'asst2_trav'))


class TestCompetitionForm(TestCase):

    def test_comp_is_required(self):
        form = CompetitionForm({'comp': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('comp', form.errors.keys())
        self.assertEqual(form.errors['comp'][0], 'This field is required.')

    def test_field_is_explicit_in_form_metaclass(self):
        form = CompetitionForm()
        self.assertEqual(form.Meta.fields, ('comp',))


class TestClubForm(TestCase):

    def test_club_name_is_required(self):
        form = ClubForm({'club_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('club_name', form.errors.keys())
        self.assertEqual(form.errors['club_name'][0], 'This field is required.')

    def test_club_badge_not_required(self):
        form = ClubForm({
            'club_name': 'Leckhampton Rovers FC',
            'club_badge': '',
            'club_badge_url': 'www.cheltenhamyouthleague.co.uk/img/cyfl/tn/leckhampton(1).jpg',
            'website_url': 'www.leckhamptonrovers.co.uk/'
            })
        self.assertTrue(form.is_valid())

    def test_club_badge_url_required(self):
        form = ClubForm({'club_badge_url': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('club_badge_url', form.errors.keys())
        self.assertEqual(form.errors['club_badge_url'][0], 'This field is required.')

    def test_website_url_required(self):
        form = ClubForm({'website_url': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('website_url', form.errors.keys())
        self.assertEqual(form.errors['website_url'][0], 'This field is required.')


class TestTeamForm(TestCase):

    def test_team_name_required(self):
        form = TeamForm({'team_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('team_name', form.errors.keys())
        self.assertEqual(form.errors['team_name'][0], 'This field is required.')

    def test_short_name_required(self):
        form = TeamForm({'short_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('short_name', form.errors.keys())
        self.assertEqual(form.errors['short_name'][0], 'This field is required.')

    def test_age_required(self):
        form = TeamForm({'age': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('age', form.errors.keys())
        self.assertEqual(form.errors['age'][0], 'This field is required.')

    def test_club_name_required(self):
        form = TeamForm({'club_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('club_name', form.errors.keys())
        self.assertEqual(form.errors['club_name'][0], 'This field is required.')

    def test_manager_coach_required(self):
        form = TeamForm({'manager_coach': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('manager_coach', form.errors.keys())
        self.assertEqual(form.errors['manager_coach'][0], 'This field is required.')


class TestGameForm(TestCase):

    def test_fields_are_excluded_from_form_metaclass(self):
        form = GameForm()
        self.assertEqual(form.Meta.exclude, ('ref_total', 'asst1_total', 'asst2_total', 'ref_trav', 'asst1_trav', 'asst2_trav'))

    def test_age_required(self):
        form = GameForm({'age': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('age', form.errors.keys())
        self.assertEqual(form.errors['age'][0], 'This field is required.')

    def test_competition_required(self):
        form = GameForm({'competition': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('competition', form.errors.keys())
        self.assertEqual(form.errors['competition'][0], 'This field is required.')

    def test_home_team_required(self):
        form = GameForm({'home_team': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('home_team', form.errors.keys())
        self.assertEqual(form.errors['home_team'][0], 'This field is required.')

    def test_away_team_required(self):
        form = GameForm({'away_team': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('away_team', form.errors.keys())
        self.assertEqual(form.errors['away_team'][0], 'This field is required.')

    def test_date_time_required(self):
        form = GameForm({'date_time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('date_time', form.errors.keys())
        self.assertEqual(form.errors['date_time'][0], 'This field is required.')

    def test_venue_required(self):
        form = GameForm({'venue': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('venue', form.errors.keys())
        self.assertEqual(form.errors['venue'][0], 'This field is required.')


class TestChatForm(TestCase):

    def test_match_is_required(self):
        form = ChatForm({'match': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('match', form.errors.keys())
        self.assertEqual(form.errors['match'][0], 'This field is required.')

    def test_author_required(self):
        form = ChatForm({'author': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('author', form.errors.keys())
        self.assertEqual(form.errors['author'][0], 'This field is required.')
