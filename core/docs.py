from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Fitness API",
        default_version="v1",
        description="API for managing workouts, users, and fitness tracking.",
        contact=openapi.Contact(email="aolie94@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
