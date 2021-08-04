from django.test import TestCase


class TestProfileViews(TestCase):

    def test_get_profile_page(self):
        response = self.client.get('/profile')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    # def test_edit_profile(self):