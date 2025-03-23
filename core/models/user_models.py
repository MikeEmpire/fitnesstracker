from django.contrib.auth.models import AbstractUser
from django.db import models
from time import timezone


class User(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.CharField(
        max_length=100, blank=True, null=True, help_text="Users personal bio"
    )
    is_trainer = models.BooleanField(
        default=False, help_text="Wether this user is a trainer"
    )

    followers = models.ManyToManyField(
        "self", related_name="following", blank=True, symmetrical=False
    )

    def __str__(self):
        return self.username

    def get_age(self):
        """Calculate user's age based on date of birth"""
        if self.date_of_birth:
            today = timezone.now().date()
            return (
                today.year
                - self.date_of_birth.year
                - (
                    (today.month, today.day)
                    < (self.date_of_birth.month, self.date_of_birth.day)
                )
            )
        return None
