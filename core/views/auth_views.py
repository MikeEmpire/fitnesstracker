from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from oauth2_provider.models import AccessToken
from django.utils.timezone import now

@login_required
def get_access_token(request):
    token = AccessToken.objects.filter(user=request.user, expires__gt=now()).first()
    if token:
        return JsonResponse({"access_token": token.token})
    return JsonResponse({"error": "No valid token found"}, status=401)