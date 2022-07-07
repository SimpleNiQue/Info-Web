from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms

from.models import InfoWebUser, PersonalDetails, WorkDetails


class NewUserForm(ModelForm):
    class Meta:
        model = InfoWebUser
        fields ='__all__'
        exclude = ['user',]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PersonalDetailsForm(ModelForm):
    class Meta:
        model = PersonalDetails
        fields = '__all__'
        exclude = ['user',]

class WorkDetailsForm(ModelForm):
    class Meta:
        model =WorkDetails
        fields = '__all__'