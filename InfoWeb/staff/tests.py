from django.test import TestCase
from django.urls import reverse

class StaffViewTests(TestCase):
    def test_home_view(self):
        """Check that home view is working"""
        home = self.client.get(reverse('staff:home'))
        self.assertEqual(home.status_code, 200)

    def test_login_view(self):
        """Check that login view works"""
        login = self.client.get(reverse('staff:login'))
        self.assertEqual(login.status_code, 200)

    def test_register_view(self):
        """Check that Register View Works"""
        register = self.client.get(reverse('staff:register'))
        self.assertEqual(register.status_code, 200)

