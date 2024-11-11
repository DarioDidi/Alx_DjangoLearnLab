from django.db.models.signals import post_init
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile


@receiver(post_init, sender=User)
def create_profile(sender, instance, created):
    if created:
        UserProfile.objects.create(user=instance)


