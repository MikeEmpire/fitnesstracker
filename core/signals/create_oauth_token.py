from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_added
from oauth2_provider.models import AccessToken, Application
from django.utils.timezone import now
from datetime import timedelta
import secrets  # For secure token generation

print("✅ Signal loaded: create_oauth_token.py")


@receiver(social_account_added)
def create_oauth_token(sender, request, sociallogin, **kwargs):
    user = sociallogin.user

    app = Application.objects.filter(client_type="public").first()
    if not app:
        return  # No OAuth2 application found

    # Check if the user already has a valid token
    existing_token = AccessToken.objects.filter(user=user, expires__gt=now()).first()
    if existing_token:
        return  # Don't create a new token if one already exists

    # Generate a new access token
    token = AccessToken.objects.create(
        user=user,
        application=app,
        expires=now() + timedelta(hours=1),
        token=secrets.token_hex(32),  # Secure token generation
    )

    # Store token in session (optional)
    request.session["oauth_token"] = token.token
