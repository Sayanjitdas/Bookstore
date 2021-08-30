from users.views import SignupPageView
from users.forms import CustomUserCreationForm
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test.utils import get_runner
from django.urls import reverse,resolve
# Create your tests here.

class CustomUserTests(TestCase):

    def test_user_create(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="will",
            email="will@email.com",
            password="will123"
        )

        self.assertEqual(user.username,"will")
        self.assertEqual(user.email,"will@email.com")
        self.assertFalse(user.is_superuser)

    def test_superuser_create(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="superadmin",
            email="superadmin@email.com",
            password="superadmin123"
        )
        
        self.assertEqual(user.username,"superadmin")
        self.assertEqual(user.email,"superadmin@email.com")
        self.assertTrue(user.is_superuser)

class SignupPageTests(TestCase):

    def setUp(self):

        self.url = reverse('signup')
        self.response = self.client.get(self.url)

    def test_signup_url_status(self):
        self.assertEqual(self.response.status_code,200)

    def test_signup_template_check(self):
        self.assertTemplateUsed(self.response,'signup.html')
    
    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form,CustomUserCreationForm)
        self.assertContains(self.response,'csrfmiddlewaretoken') 

    def test_signup_view(self):
        view = resolve(self.url)
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__
        )       