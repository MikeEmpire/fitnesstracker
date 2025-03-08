import logging
from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_added
from oauth2_provider.models import AccessToken, Application
from django.utils.timezone import now
from datetime import timedelta
import secrets  # For secure token generation

logger = logging.getLogger(__name__)


@receiver(social_account_added)
def create_oauth_token(sender, request, sociallogin, **kwargs):
    user = sociallogin.user
    logger.info(f"Signal triggered for user: {user}")

    app = Application.objects.filter(client_type="public").first()
    if not app:
        logger.warning("No OAuth2 application found.")
        return  # No OAuth2 application found

    # Check if the user already has a valid token
    existing_token = AccessToken.objects.filter(user=user, expires__gt=now()).first()
    if existing_token:
        request.session["oauth_token"] = existing_token.token
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
