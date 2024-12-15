from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts_app.models.user_manager import CustomUserManager


class Customer(AbstractUser):
    username = None
    email = models.EmailField(max_length=254, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        """
        Returns a string representation of the Customer instance.
        """
        return f"{self.email} (ID: {self.id})"
