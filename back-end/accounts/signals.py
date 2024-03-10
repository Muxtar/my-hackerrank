from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import WaitGroup, Group


@receiver(post_save, sender = WaitGroup)
def my_handler(sender, instance, created, **kwargs):
    if not created and instance.agree:
        instance.group.student.add(instance.user)
        instance.delete()
