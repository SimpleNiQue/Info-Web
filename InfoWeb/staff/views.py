#* Django imports
from typing import Optional
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group        
#====================================================

# My imports
from .models import PersonalDetails
from .forms import PersonalDetails, CreateUserForm, PersonalDetailsForm, WorkDetailsForm
from .decorators import allowed_users, unauthenticated_user
from django.views.generic import ListView, DetailView
#==============================================================



class IndexView(ListView):
    template_name: str = 'staff/index.html'
    context_object_name: Optional[str] = 'personal_details'

    def get_queryset(self):
        return PersonalDetails.objects.all()

# TODO: Bring back unauthentication decorator
def login_user(request):
  if request.method =='POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
      
    print(username)  
    user = authenticate(request, username=username, password=password)
    print(user)
      
    if user is not None:
      login(request, user)
      print(username, 'logged in')
      return redirect('staff:home')
      
    else: messages.error(request, 'Account not Registered')
  
  return render(request, 'staff/login.html')

#Logout
@login_required(login_url='staff:login')
def log_out(request):
  logout(request)
  print(request.user.username, 'logged out')
  return render(request,'staff/index.html')

# Registers a new user
# TODO: Bring back unauthentication decorator
def register(request):
  form = CreateUserForm()
    
  if request.method=='POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get('username')
      
      
      messages.success(request," Account was Created for "+username)
      return redirect('staff:login')
    else:
      messages.error(request, 'Incorrect credentials')
        
  context = {'form':form}
  return render(request,'staff/register.html', context)
