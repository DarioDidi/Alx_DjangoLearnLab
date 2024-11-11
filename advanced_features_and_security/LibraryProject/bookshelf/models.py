from django.db import models
from django.contrib.auth.models import AbstractUser

"class CustomUser(AbstractUser):", "date_of_birth", "profile_photo"
# Create your models here.


class User(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        # if not email:
        #     raise ValueError(_('Users must have an email address'))
        # email = self.normalize_email(email)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

# class SomethingElse(models.Model):
#     name = models.CharField(max_length=10)
