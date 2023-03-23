from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from apps.users.managers import CustomUserManager
from django.utils import timezone

# Create your models here.

class User(AbstractBaseUser):
    USER_TYPE = [
        ('owner', 'Owner'),
        ('superuser', 'Superuser'),
    ]

    user_type = models.CharField(max_length=10, choices=USER_TYPE)

    email = models.EmailField("email address", unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.user_type == 'owner':
            self.is_owner = True
        elif self.user_type == 'superuser':
            self.is_superuser = True
            self.is_staff = True
        super().save(*args, **kwargs)