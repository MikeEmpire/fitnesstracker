"""
URL configuration for fitnesstracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from core.docs import schema_view
from django.contrib import admin
from django.urls import path, re_path, include

DJANGO_API_VERSION = 1

urlpatterns = [
    path("admin/", admin.site.urls),
    path(f"api/v{DJANGO_API_VERSION}/", include("core.urls")),
    # 📌 Swagger documentation
    path("api/docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api-docs"),
    path("api/redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="redoc"),
    # 📌 JSON & YAML schema URLs (for programmatic API access)
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    )
]
