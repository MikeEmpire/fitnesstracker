import pytest


@pytest.mark.django_db
def test_unauthorized_request(api_client):
    """Ensure unauthorized users cannot access protected endpoints"""
    response = api_client.get("/api/v1/workouts")
    assert response.status_code == 401
