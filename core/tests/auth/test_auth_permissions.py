import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_unauthorized_request():
    """Ensure unauthorized users cannot access protected endpoints"""
    unauthorized_api_client = APIClient()
    response = unauthorized_api_client.get("/api/v1/workouts/")
    assert response.status_code == 401


@pytest.mark.django_db
def test_authorized_request(api_client):
    """Ensure authorized users can access protected endpoints"""
    response = api_client.get("/api/v1/workouts/")
    assert response.status_code == 200
