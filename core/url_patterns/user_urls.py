from django.urls import path
from core.views.user_views import UserView


urlpatterns = [
    path("users/", UserView.as_view(), name="users"),
]
