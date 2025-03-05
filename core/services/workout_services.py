import re
from django.conf import settings
from django.utils.timezone import now
from core.models.workout_models import Exercise, WorkoutPlan, WorkoutSession
from core.types import WorkoutPreferences
from openai import OpenAI


def create_default_workout(user):
    return WorkoutPlan.objects.create(
        user=user, name="Starter Plan", goal="general_fitness"
    )


def generate_workout_plan(user, preferences: WorkoutPreferences) -> dict:
    """
    Generates a workout plan using OpenAI's GPT-4 based on user preferences.

    Args:
        preferences (WorkoutPreferences): A dictionary containing user preferences.

    Returns:
        dict: The response from OpenAI containing the generated workout plan.
    """
    api_key = getattr(settings, "OPENAI_API_KEY", None)
    if not api_key:
        raise ValueError("OPENAI_API_KEY not set in settings")

    client = OpenAI(api_key=api_key)

    prompt = f"""
    Create a {preferences["fitness_goal"]} workout plan for a {preferences["experience_level"]} level individual.
    The person has {preferences["days_per_week"]} workout days per week.
    They will be working out at {preferences["workout_location"]}.
    If home, they have this equipment: {preferences["available_equipment"]}.
    Include workout sessions, exercises, sets and reps.
    """

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o",
    )

    return save_workout_plan(user, response)


def save_workout_plan(user, openai_response):
    """
    Parses OpenAI's generated workout plan and saves it to the database.

    Args:
        user (User): The user who owns the workout plan.
        openai_response (dict): The response from OpenAI containing the generated workout plan.

    Returns:
        WorkoutPlan Instance.
    """
    try:
        workout_text = openai_response.choices[0].message.content

        goal_match = re.search(r"Creating a (.*?) workout plan", workout_text)
        goal = goal_match.group(1) if goal_match else "General Fitness"
        goal = goal.lower().replace(" ", "_")

        workout_plan = WorkoutPlan.objects.create(
            user=user,
            name="AI Generated Plan",
            goal=goal,
            created_at=now(),
            updated_at=now(),
            deleted_at=None,
            duration=4,
        )
        session_matches = re.findall(
            r"### (Day \d+ .+?)\n\n- \*\*Warm-up", workout_text
        )
        days_mapping = [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
        ]
        for index, session_text in enumerate(session_matches):
            session_name_match = re.match(r"Day \d+: (.*)", session_text)
            session_name = (
                session_name_match.group(1) if session_name_match else "Unknown Session"
            )

            day_of_week = days_mapping[index % len(days_mapping)]

            workout_session = WorkoutSession.objects.create(
                workout_plan=workout_plan, name=session_name, day_of_week=day_of_week
            )

            exercises = re.findall(
                r"\d+\.\s(.*?):\s(\d+)\ssets\sx\s(\d+)\sresps", workout_text
            )
            for exercise_name, sets, reps in exercises:
                Exercise.objects.create(
                    workout_session=workout_session,
                    name=exercise_name.strip(),
                    sets=int(sets),
                    reps=int(reps),
                    rest_time=60,
                    muscle_group="full_body",
                )
        return workout_plan

    except Exception as e:
        print(f"Error saving workout plan: {e}")
        return None
