from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from apps.users.models import Profile


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        print('Creating Profile....')
        user = instance
        Profile.objects.create(
            user=instance,
            username=user.username,
            email=user.email,
            name=user.first_name
        )
    else:
        pass


@receiver(post_save, sender=Profile)
def updateUser(sender, instance, created, **kwargs):
    if created is False:
        print('Editing User....')
        profile = instance
        user = profile.user
        user.username = profile.username
        user.email = profile.email
        user.first_name = profile.name
        user.save()


@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    print('Deleting User....')
    try:
        user = instance.user
        user.delete()
    except:
        pass


