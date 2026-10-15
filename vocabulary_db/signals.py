from django.db.models.signals import post_delete, pre_save
from django.dispatch.dispatcher import receiver

from .models import *


@receiver(post_delete, sender=Source)
def source_post_delete(sender, instance, **kwargs) :
    if instance.image and not Source.objects.filter(image=instance.image.name).exists() :
        instance.image.delete(False)

@receiver(pre_save, sender=Source)
def source_pre_save(sender, instance, **kwargs) :
    if instance.pk :
        try :
            old_image = sender.objects.get(pk=instance.pk).image
            if old_image != instance.image and not Source.objects.filter(image=instance.image.name).exists() :
                old_image.delete(False) 
        except Source.DoesNotExist :
            pass
