from django.test import TestCase
from .forms import UserProfileForm


class TestUserProfileForm(TestCase):

    def test_fields_are_excluded_in_form_metaclass(self):
        form = UserProfileForm()
        self.assertEqual(form.Meta.exclude, ('user', 'role'))

    def test_profile_phone_number_is_not_required(self):
        form = UserProfileForm({'profile_phone_number': ''})
        self.assertTrue(form.is_valid())

    def test_profile_street_address1_is_not_required(self):
        form = UserProfileForm({'profile_street_address1': ''})
        self.assertTrue(form.is_valid())

    def test_profile_street_address2_is_not_required(self):
        form = UserProfileForm({'profile_street_address2': ''})
        self.assertTrue(form.is_valid())

    def test_town_or_city_is_not_required(self):
        form = UserProfileForm({'profile_town_or_city': ''})
        self.assertTrue(form.is_valid())

    def test_profile_county_is_not_required(self):
        form = UserProfileForm({'profile_county': ''})
        self.assertTrue(form.is_valid())

    def test_profile_postcode_is_not_required(self):
        form = UserProfileForm({'profile_postcode': ''})
        self.assertTrue(form.is_valid())

    def test_profile_country_is_not_required(self):
        form = UserProfileForm({'profile_country': ''})
        self.assertTrue(form.is_valid())
