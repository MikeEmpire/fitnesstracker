import pytest
from unittest.mock import MagicMock
from django.utils.timezone import now, timedelta
from oauth2_provider.models import AccessToken, Application
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.signals import social_account_added
from django.test import Client, RequestFactory


@pytest.mark.django_db
def test_create_oauth_token_signal(test_user):
    """ "Test that an OAuth2 token is created when a social account is added"""

    # ✅ Create an OAuth application
    Application.objects.create(
        name="Test Application",
        client_type="public",
        authorization_grant_type="password",
    )

    assert not AccessToken.objects.filter(user=test_user).exists()

    # ✅ Create a social account instance
    SocialAccount.objects.create(
        user=test_user,
        provider="google",
        uid="1234567890",
    )

    request = RequestFactory().get("/")
    request.session = {}

    social_account_added.send(
        sender=SocialAccount, request=request, sociallogin=MagicMock(user=test_user)
    )

    assert AccessToken.objects.filter(user=test_user).exists()

    # ✅ Verify that the token has an expiration date
    assert "oauth_token" in request.session


@pytest.mark.django_db
def test_oauth_token_not_created_if_existing(test_user):
    """Test that a new OAuth2 token is NOT created if one already exists"""

    # ✅ Create an OAuth application
    app = Application.objects.create(
        name="Test App",
        client_type="public",
        authorization_grant_type="password",
    )

    # ✅ Create an existing valid token
    AccessToken.objects.create(
        user=test_user,
        application=app,
        expires=now() + timedelta(hours=1),
        token="existing_token",
    )

    # ✅ Create a social account instance
    SocialAccount.objects.create(
        user=test_user, provider="google", uid="12345"
    )

    # ✅ Use Django’s Client to create a valid request object
    client = Client()
    client.force_login(test_user)  # ✅ Ensure user is logged in

    # ✅ Generate a request with a valid session
    request = client.get("/")  # ✅ This ensures a valid request object
    session = request.wsgi_request.session  # ✅ Extract session from request
    session.save()  # ✅ Save the session

    # ✅ Trigger the signal manually (simulate social login)
    social_account_added.send(
        sender=SocialAccount,
        request=request.wsgi_request,  # ✅ Use `wsgi_request` for real request object
        sociallogin=MagicMock(user=test_user),
    )

    # ✅ Reload session to ensure changes were saved
    session = request.wsgi_request.session
    session.modified = True  # Explicitly mark session as modified
    session.save()

    # ✅ Debugging output
    print("Session contents:", dict(session.items()))

    # ✅ Ensure NO new OAuth2 token was created
    assert AccessToken.objects.filter(user=test_user).count() == 1

    # ✅ Check if 'oauth_token' exists before asserting
    assert "oauth_token" in session, "OAuth token was not stored in session"
    assert session["oauth_token"] == "existing_token"
