from django.urls import path
from core.views.tracking_views import ChecklistView


urlpatterns = [
    path("checklists/", ChecklistView.as_view(), name="checklists"),
]
