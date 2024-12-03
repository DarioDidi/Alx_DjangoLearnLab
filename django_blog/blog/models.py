from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_init, post_save
from django.dispatch import receiver

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + self.content

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    email = models.EmailField()
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    

    # role = models.CharField(max_length=50, choices=[
    #     ('Admin', "administrator"), ('Librarian', "librarian"), ('Member',"member")])


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile.objects.create(user=instance)
        user_profile.save()