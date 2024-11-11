from django.db import models
from django.db.models.signals import post_init, post_save
from django.dispatch import receiver
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.base_user import BaseUserManager
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL

# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password, **extra_fields):
#         # if not email:
#         #     raise ValueError(_('Users must have an email address'))
#         # email = self.normalize_email(email)
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save()

#         return user

#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError(_('Superuser must have is_staff=True.'))
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(_('Superuser must have is_superuser=True.'))
#         return self.create_user(email, password, **extra_fields)


# class CustomUser(AbstractUser):
#     date_of_birth = models.DateField()
#     profile_photo = models.ImageField()

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        default_permissions = ()
        permissions = (
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        )

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
    role = models.CharField(max_length=50, choices=[
        ('Admin', "administrator"), ('Librarian', "librarian"), ('Member', "member")])


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile.objects.create(user=instance)
        user_profile.save()
