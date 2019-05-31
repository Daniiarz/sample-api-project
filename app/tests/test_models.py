from django.contrib.auth import get_user_model
from django.test import TestCase
from core import models

PASSWORD = 'Qwertyz01'


def sample_user(email='test@londonappdev.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


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

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )
        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """Test the recipe string representation"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Steak and mushroom sauce',
            time_minutes=5,
            price=5.00
        )

        self.assertEqual(str(recipe), recipe.title)
