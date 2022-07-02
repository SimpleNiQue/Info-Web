from django.db.models.signals import post_save
from django.contrib.auth.models import User

from django.contrib.auth.models import Group
from .models import InfoWebUser


def staff_profile(sender, instance, created, **kwargs):
  if created:
    group = Group.objects.get(name='staff')
    instance.groups.add(group)
    
    InfoWebUser.objects.create(name=instance.username)
    print('\nStaff Created\n')
    
post_save.connect(staff_profile, sender=User)
  