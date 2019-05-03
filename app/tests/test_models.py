from django.contrib.auth import get_user_model
from django.test import TestCase

PASSWORD = 'Qwertyz01'


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'da@da.com'

        user = get_user_model().objects.create_user(
            email=email,
            password=PASSWORD
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(PASSWORD))

    def test_user_normalized_email(self):
        """Test creation of user with normalized email"""
        email = "da@DA.COM"
        user = get_user_model().objects.create_user(email, PASSWORD)

        self.assertEqual(user.email, email.lower())

    def test_user_creation_without_email(self):
        """Test user created without email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, PASSWORD)

    def test_create_superuser(self):
        """Test creation of superuser"""
        user = get_user_model().objects.create_superuser(
            "da@da.com",
            PASSWORD
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
