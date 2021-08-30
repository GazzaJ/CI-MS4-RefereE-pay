from django.test import TestCase
from django.contrib.auth.models import User


class TestProfileViews(TestCase):
    def test_get_profile_page(self):
        User.objects.create_user(
            'testuser',
            'test@email.com',
            'testpassword'
        )

        self.client.login(
            username='testuser',
            password='testpassword'
        )

        response = self.client.get("/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertTemplateUsed(response, 'base.html')
