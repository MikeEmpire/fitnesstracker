from typing import TypedDict


class WorkoutPreferences(TypedDict):
    fitness_goal: str
    experience_level: str
    days_per_week: int
    workout_location: str
    available_equipment: list[str]
