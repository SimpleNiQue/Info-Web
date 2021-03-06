from django.db import models
from django.contrib.auth.models import User
from .utils import DEPT, ALL_LGA, GENDER,MARITAL_STATUS,STATES, ID_COLLECTED, GL_and_STEP
# TODO Remember to change null field values to False later i.e 'null=False'


class WorkDetails(models.Model):
    """Work Details for a paticular Staff"""

    class Meta:
        verbose_name_plural = 'Work Details'

    ID_number= models.CharField(max_length=25, primary_key=True, blank=False, unique=True, null=False)
    file_number = models.CharField(max_length=50, unique=True, blank=True, null=True)
    department = models.CharField(choices=(DEPT), max_length=50, null=True, blank=True)
    ID_card= models.CharField(choices=ID_COLLECTED, null=True, blank=True, max_length=5)

    state_directorate=  models.CharField(choices=(STATES), max_length=50, null=True, blank=True) 
    date_of_first_appointment = models.DateField(null=True, blank=True)
    # date_of_present_appointment = models.DateField(null=True, blank=True)
    rank = models.CharField(max_length=50, null=True, blank=True)
    
    
    qualification = models.CharField(max_length=300, null=True, blank=True)
    remarks = models.CharField(max_length=500, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ID_number

class PersonalDetails(models.Model):
    """Personal details about a particular Staff"""

    class Meta:
        verbose_name_plural = 'Personal Details'

    work_id_number = models.OneToOneField(WorkDetails, on_delete=models.CASCADE, related_name='personal_detail')
    surname = models.CharField(max_length=250, null=True, blank=True,)
    first_name = models.CharField(max_length=250, null=True, blank=True,)
    
    middle_name = models.CharField(max_length=250, null=True, blank=True,)
    gender = models.CharField(max_length=10, choices=GENDER)
    date_of_birth = models.DateField(null=True, blank=True)
    marital_status = models.CharField(choices=(MARITAL_STATUS), max_length=10, null=True, blank=True)
    
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    state_of_origin = models.CharField(choices=STATES, max_length=50, null=True, blank=True)
    lga =  models.CharField(choices=(ALL_LGA), max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='upload/', default='profile1.png', null=True, blank=True)
    

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    def __str__(self):
        return self.first_name


class LinkedAccount(models.Model):
    """Every User that has been Registered and Linked to an account"""

    class Meta:
        verbose_name_plural = 'Linked Accounts'

    user =models.ForeignKey(User, on_delete=models.CASCADE, related_name='linked_account')

    def __str__(self):
        return str(self.user)
    
