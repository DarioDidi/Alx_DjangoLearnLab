from django.db import models
from django.contrib.auth.models import AbstractUser

"class CustomUser(AbstractUser):", "date_of_birth", "profile_photo"
# Create your models here.


class User(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

# class SomethingElse(models.Model):
#     name = models.CharField(max_length=10)
