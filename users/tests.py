from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test.utils import get_runner
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