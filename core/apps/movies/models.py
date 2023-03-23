from django.db import models
from apps.users.models import User

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movie_user')
    tags = models.ManyToManyField(Tag, related_name='movie_tags')

    def __str__(self) -> str:
        return self.title