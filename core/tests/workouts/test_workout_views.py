import pytest
from core.models.workout_models import WorkoutPlan
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from unittest.mock import patch, MagicMock


@pytest.mark.django_db
def test_generate_invalid_workout_plan(api_client):
    """Test creating an invalid workout plan to make sure decorators work"""
    invalid_data = {
        "experience_level": "beginner",  # Missing "fitness_goal"
        "days_per_week": 4,
        "workout_location": "gym",
        "available_equipment": ["treadmill"],
    }
    response = api_client.post(
        "/api/v1/workouts/generate-workout/", invalid_data, format="json"
    )
    assert response.status_code == HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_generate_workout_plan_mocked(api_client, test_user):
    """Test generating a workout plan while mocking OpenAI API"""

    valid_data = {
        "fitness_goal": "muscle_gain",
        "experience_level": "beginner",
        "days_per_week": 4,
        "workout_location": "home",
        "available_equipment": ["dumbbells", "resistance bands"],
    }

    # ✅ Mock OpenAI API for testing purposes
    with patch("core.services.workout_services.OpenAI") as mock_openai:
        mock_client = MagicMock()
        mock_openai.return_value = mock_client  # ✅ Mock OpenAI client

        # ✅ Ensure the response is structured like OpenAI actually returns
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message = MagicMock()
        mock_response.choices[0].message.content = "Created a muscle_gain workout plan"

        # ✅ Mock OpenAI's API response
        mock_client.chat.completions.create.return_value = mock_response

        # ✅ Call API
        response = api_client.post(
            "/api/v1/workouts/generate-workout/",
            valid_data,
            format="json",
        )

        assert response.status_code == HTTP_201_CREATED  # ✅ Expect successful creation
        assert "plan_id" in response.json()  # ✅ Expect a generated plan ID

        # ✅ Ensure a workout plan is saved to the database
        assert WorkoutPlan.objects.count() == 1


@pytest.mark.django_db
def test_workout_plan_list(api_client):
    """Test that a user is able to get a list of workout plans"""
    response = api_client.get("/api/v1/workouts/")
    assert response.status_code == HTTP_200_OK
