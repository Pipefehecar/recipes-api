"""
Test for the django admin modifications.
"""
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Test the admin site."""

    def setUp(self):
        """Setup."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser('admin@example.com', 'password123')
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user('user@example.com', 'password123', name='Test User')

    def test_users_listed(self):
        """Test that users are listed on user page."""
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_edit_user_page(self):
        """Test that the edit user page works."""
        url = reverse('admin:core_user_change', args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works."""
        url = reverse('admin:core_user_add')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
