# From https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
import os

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    hours_worked = models.IntegerField(default=0)
    profile_image = models.ImageField(
        upload_to=get_image_path, blank=True, null=True)

    @property
    def get_prof_pic_url(self):
        return '/static/login/images/icons/default-profile-picture.jpg'


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
