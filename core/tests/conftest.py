import os
import django
import factory
import pytest
from core.models.workout_models import WorkoutPlan
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from oauth2_provider.models import AccessToken, Application
from django.utils.timezone import now
from datetime import timedelta
import secrets

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fitnesstracker.settings")
django.setup()


# Ensure Django settings are loaded before anything else

User = get_user_model()


# ✅ User Factory
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        skip_postgeneration_save = True # ✅ Prevents user factory from saving twice

    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "securepass")


# ✅ Workout Factory
class WorkoutPlanFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WorkoutPlan

    name = "Test App"
    goal = "strength"
    duration = 5000


# ✅ OAuth2 Application Factory
class OAuthApplicationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Application

    name = "Test App"
    client_type = "public"
    authorization_grant_type = "password"


# ✅ OAuth2 Token Factory
class OAuthTokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AccessToken

    user = factory.SubFactory(UserFactory)
    application = factory.SubFactory(OAuthApplicationFactory)
    expires = factory.LazyFunction(lambda: now() + timedelta(hours=1))
    token = factory.LazyFunction(lambda: secrets.token_hex(32))


@pytest.fixture
def test_user(db):
    """Creates and returns a test user"""
    return UserFactory()


@pytest.fixture
def test_workout_plan(db):
    return WorkoutPlanFactory()


# ✅ Database access for all tests
@pytest.fixture(scope="function")
def db():
    """Ensure database access for tests using pytest-django"""
    return


# ✅ Create an authenticated API client
@pytest.fixture
def api_client(test_user):
    """Returns an API Client authenticated as test_user"""
    client = APIClient()
    client.force_authenticate(user=test_user)
    return client


# ✅ Create an OAuth2 application (for issuing tokens)
@pytest.fixture
def oauth_application(db):
    """Returns an OAuth2 Application for testing"""
    return OAuthApplicationFactory()


# ✅ Generate an OAuth2 token for a user
@pytest.fixture
def access_token(test_user, oauth_application):
    """Creates and returns an OAuth2 access token"""
    return OAuthTokenFactory(user=test_user, application=oauth_application)
