from django.db import models
from core.models.user_models import User


class Trainer(models.Model):
    """

    Args:
        models (_type_): _description_
    """

    user = models.OneToOneField()
