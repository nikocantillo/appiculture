"""Users models."""

# Django
from django.contrib.auth.models import User
from django.db import models


class User(models.Model):
    """Profile model.

    Proxy model that extends the base data with other
    information.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'user'

    def __str__(self):
        """Return username."""
        return self.user.username