from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User


# @receiver(post_save, sender=Profile)
def create_profile(sender, instance,created, **kwargs):
    print('Profile seved')

    if created:
        user = instance
        profile = Profile.objects.create(user=user,
                                         username=user.username,
                                         email=user.email,
                                         name=user.first_name,
                                         )

# @receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()

def update_user(sender, instance, created, **kwargs):
    profile = instance
    user = instance.user

    if created is False:
        user.username = profile.username
        user.email = profile.email
        user.first_name = profile.name
        user.save()


# ВМЕСТО ВЫЗОВОВ ФУНКЦИИ ДОБАВИЛИ ДЕКОРАТОР!!!


post_save.connect(create_profile, sender=User)
post_delete.connect(delete_user, sender=Profile)
post_save.connect(update_user, sender=Profile)
