from django.contrib import admin
from.models import LinkedAccount, WorkDetails, PersonalDetails

admin.site.register(PersonalDetails)
admin.site.register(WorkDetails)
admin.site.register(LinkedAccount)

