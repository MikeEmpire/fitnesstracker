from django.test import TestCase
from core.models.user_models import User

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username="testuser", email="test@example.com")
        self.assertEqual(user.username, "testuser")
