import os
from core.models.workout_models import WorkoutPlan
from openai import OpenAI


def create_default_workout(user):
    return WorkoutPlan.objects.create(
        user=user, name="Starter Plan", goal="general_fitness"
    )


def generate_workout_plan(user):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    preferences = user.preferences

    prompt = f"""
    Create a {preferences.fitness_goal} workout plan for a {preferences.experience_level} level individual.
    The person has {preferences.days_per_week} workout days per week.
    They will be working out at {preferences.workout_location}.
    If home, they have this equipment: {preferences.available_equipment}.
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

    print(response)
