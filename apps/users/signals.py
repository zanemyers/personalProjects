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
            name=user.first_name + ' ' + user.last_name,
        )
    else:
        user = Profile.objects.get(user=instance)
        user.user = instance
        user.username = instance.username
        user.email = instance.email
        user.name = instance.first_name + ' ' + instance.last_name
        user.save()


@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    print('Deleting User....')
    user = instance.user
    user.delete()