from __future__ import annotations
from typing_extensions import NotRequired
from typing import TypedDict


class WorkoutPreferences(TypedDict):
    fitness_goal: str
    experience_level: str
    days_per_week: int
    workout_location: str
    available_equipment: NotRequired[list[str]]
