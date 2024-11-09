from django.db import models
from django.db.models.signals import post_init
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Library(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=50)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices= ['Admin','Librarian','Member'])

@receiver(post_init, sender=User)
def create_profile(sender, instance, created):
    if created:
        user_profile = UserProfile.objects.create(user=instance)
        user_profile.save()