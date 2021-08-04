from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import User, UserProfile
from .forms import UserProfileForm


class TestProfileViews(TestCase):    

    def test_get_profile_page(self):
        user = User.objects.create_user(
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
