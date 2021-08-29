from pages.views import HomePageView
from django.http import response
from django.test import TestCase
from django.urls import reverse,resolve
from . import views

# Create your tests here.
class HomepageTests(TestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code,200)

    def test_homepage_template_used(self):
        self.assertTemplateUsed(self.response,'home.html')

    def test_homepageview_resolve(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__,views.HomePageView.as_view().__name__)
