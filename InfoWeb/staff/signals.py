from unicodedata import name
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from .models import PersonalDetails, WorkDetails

def staff_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='staff')
        instance.groups.add(group)
        PersonalDetails.objects.create(
            user=instance,
			name=instance.username,
        )

        print(f"\n New Staff Created and added to {group}")


post_save.connect(staff_profile, sender=User)