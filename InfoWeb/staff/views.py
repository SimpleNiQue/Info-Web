#* Django imports
from typing import Optional
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group        
#====================================================

# My imports
from .models import InfoWebUser, PersonalDetails, WorkDetails
from .forms import PersonalDetails, CreateUserForm, NewUserForm
from .decorators import allowed_users, unauthenticated_user
from django.views.generic import ListView, DetailView

from staff import models
#==============================================================



class IndexView(ListView):
    template_name: str = 'staff/index.html'
    context_object_name: Optional[str] = 'personal_details'

    def get_queryset(self):
        return PersonalDetails.objects.all()


@login_required(login_url='staff:login')
def dashboard(request, pk):
  personal = InfoWebUser.objects.get(id=pk)

  context = {
    'personal':personal
  }
  return render(request, 'staff/dashboard.html', context)


@unauthenticated_user
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
      return redirect('staff:dashboard', pk=user.id)
      
    else: messages.error(request, 'Account not Registered')
  
  return render(request, 'staff/login.html')

#Logout
@login_required(login_url='staff:login')
def log_out(request):
  logout(request)
  print(request.user.username, 'logged out')
  return HttpResponse("You Have Been Logged out")


# Registers a new user
@unauthenticated_user
def register(request):
  form = CreateUserForm()
    
  if request.method=='POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      
      messages.success(request," Account was Created for "+username)
      return redirect('staff:login')
    else:
      messages.error(request, 'Incorrect credentials')
        
  context = {'form':form}
  return render(request,'staff/register.html', context)





@login_required(login_url='staff:login')
def add_user_profile(request, user):
  personal_details = PersonalDetails.objects.all()
  # if this is a POST request we need to process the form data
  if request.method == 'POST':
    # create a form instance and populate it with data from the request:
    form = NewUserForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
      # process the data in form.cleaned_data as required
      # ...

      # Get the data from the form
      user_id = str(form.cleaned_data['id'])
      file_number = form.cleaned_data['file_number']
      first_name = form.cleaned_data['first_name']

      #Check if the data corresponds from the database
      print(f'{user_id=}')
      work_details = WorkDetails.objects.get(file_number=file_number)
      print(f"/n/n{work_details.personaldetails_set.first_name}")
      
      try:
        ID, FILE, FNAME = (work_details.ID_number,work_details.file_number, work_details.personaldetails_set.first_name)

      except AttributeError as err:
        print(f"{err=}")
 
      if any(id==ID, file_number==FILE, first_name==FNAME):
        form.save()
        print("\nNew User Added/Linked")
        return redirect('staff:dashboard', pk=user.id)
      else:
        messages.error(request, "such User does not exist")
        print("\nError")

      # redirect to a new URL:
      return redirect('staff:dashboard')

  # if a GET (or any other method) we'll create a blank form
  else:
      form = NewUserForm()

  return render(request, 'staff/link_profile.html', {'form': form})
