
from django.forms import CharField, ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms

from.models import LinkedAccount, PersonalDetails, WorkDetails


class LinkAccountForm(forms.Form):
    """Form for Linking Users to their Details"""
    id_number = forms.CharField(max_length=200)
    first_name = forms.CharField(max_length=200)

    def save(self, user):
        linked = LinkedAccount.objects.create(user=user)
        linked.save()

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