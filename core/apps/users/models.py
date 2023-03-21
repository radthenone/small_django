from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# class Profile(AbstractUser):
#     USER_TYPE_CHOICES = (
#         ('moderator', 'Moderator'),
#         ('regular', 'Regular'),
#     )
#     user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=10, default='regular')

# from rest_framework.permissions