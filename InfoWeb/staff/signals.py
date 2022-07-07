from django.db.models.signals import post_save
from django.contrib.auth.models import User

from django.contrib.auth.models import Group
from .models import InfoWebUser


def link_staff_profile(sender, instance, created, **kwargs):
  if created:
    user = InfoWebUser(user=instance)
    
    InfoWebUser.objects.create(user=instance, name=instance.username)
    print('\nLink added\n')
    
post_save.connect(link_staff_profile, sender=User)
  