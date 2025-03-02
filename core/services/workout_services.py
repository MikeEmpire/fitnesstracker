from core.models.workout_models import WorkoutPlan

def create_default_workout(user):
    return WorkoutPlan.objects.create(user=user, name="Starter Plan", goal="general_fitness")
