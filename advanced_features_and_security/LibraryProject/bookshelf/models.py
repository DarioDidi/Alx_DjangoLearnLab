from django.apps import AppConfig
from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group

# Create your models here.
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
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

    objects = CustomUserManager()
    # ''' can_view, can_create, can_edit, and can_delete'''
    # class Meta:
    #     default_permissions = ()
    #     permissions = (
    #         ("can_view", "Can view book"),
    #         ("can_edit_book", "Can edit book"),
    #         ("can_delete_book", "Can delete book"),
    #         ("can_create", "Can create book"),
    #     )


permissions = [
    ("can_view", "Can view book"),
    ("can_edit", "Can edit book"),
    ("can_delete", "Can delete book"),
    ("can_create", "Can create book"),
]


def create_perm(tpl):
    cdnm, nm = tpl
    Permission.objects.create(codename=cdnm, name=nm)


# class BookshelfConfig(AppConfig):
    # def ready(self):
    #     permissions = map(create_perm, permissions)

    #     Editors, created = Group.objects.get_or_create(name='Editors')
    #     Viewers, created = Group.objects.get_or_create(name='Viewers')
    #     Admins, created = Group.objects.get_or_create(name='Admins')

    #     can_view_permission = Permission.objects.get(codename='can_view')
    #     can_create_permission = Permission.objects.get(codename='can_create')
    #     can_delete_permission = Permission.objects.get(codename='can_delete')
    #     can_edit_permission = Permission.objects.get(codename='can_edit')

    #     Editors.permissions.add(can_view_permission, can_edit_permission)
    #     Viewers.permissions.add(can_view_permission)
    #     Admins.permissions.add(can_view_permission, can_delete_permission,
    #                            can_create_permission, can_edit_permission)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

# class SomethingElse(models.Model):
#     name = models.CharField(max_length=10)
