from django.test import TestCase
from django.contrib.auth.models import User


class TestHomePageViews(TestCase):

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_get_account_signup(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_new_user_signup(self):
        response = self.client.post(
            '/accounts/signup/',
            {
                'email': 'test@email.com',
                'email2': 'test@email.com',
                'username': 'testuser',
                'password': 'testpass',
                'password2': 'testpass'
            }
        )
        self.assertEqual(response.status_code, 200)

    def test_get_account_login(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_user_account_login(self):
        user = User.objects.create_user(
            'testuser',
            'test@email.com',
            'testpass123'
        )

        self.client.login(
            username='testuser',
            password='testpass123'
        )

        response = self.client.get('/accounts/login/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
