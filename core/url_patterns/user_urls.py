from django.urls import path
from core.views.user_views import UserListView


urlpatterns = [
    path("", UserListView.as_view(), name="users"),
]
