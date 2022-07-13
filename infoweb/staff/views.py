#* Django imports
from typing import Optional
from zoneinfo import available_timezones
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group        
#====================================================

# My imports
from .models import LinkedAccount, PersonalDetails, WorkDetails
from .forms import LinkAccountForm, PersonalDetails, CreateUserForm
from .decorators import allowed_users, unauthenticated_user
from django.views.generic import ListView, DetailView

#==============================================================

@unauthenticated_user
def index(request):
  context = {}
  return render(request, 'staff/index.html', context)



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
      return redirect('staff:dashboard', pk=str(request.user.id))
      
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
def dashboard(request, pk, **kwarg):
  context: dict = {}

  if str(request.user.id) == str(pk):

    try:
      work = WorkDetails.objects.get(user=pk)
      context['work'] = work
      
    except Exception as error:
      print(f"{error=}")
      return redirect('staff:link_account')

  else:
    print(f'Please Login First, request.user:{request.user}, pk:{pk}')
    return HttpResponse("Please Login First")
  
  return render(request, 'staff/dashboard.html', context)



@login_required(login_url='staff:login')
def link_account(request):
  available_linked_users = [ str(name) for name in LinkedAccount.objects.all()]
  
  if request.method == 'POST':

    #Check if account was linked before now to avoid duplicates
    if str(request.user) in available_linked_users:
      return redirect('staff:dashboard', pk=request.user.id)

    else: 
      form = LinkAccountForm(request.POST)
      if form.is_valid():
      
        collected_user_id = form.cleaned_data['id_number']
        collected_first_name = form.cleaned_data['first_name']

        #Check if the data corresponds from the database  
        try:
          work_details = WorkDetails.objects.get(user=request.user)
          ID, FILE = (work_details.ID_number, work_details.personal_detail.first_name,)

        except AttributeError as err:
          messages.error(request, "such User does not exist")
          print(f"{err=}")

        else:
    
          if (ID==collected_user_id and FILE==collected_first_name):
            form.save(request.user)
            print("\nNew User Added/Linked")
          
            return redirect('staff:dashboard', pk=request.user.id, user=request.user) 
          
          else:
            messages.error(request, "Invalid Credentials !!!")
  

    # if a GET (or any other method) we'll create a blank form
  else:

    #Check if account was linked before now to avoid duplicates
    if str(request.user) in available_linked_users:
      return redirect('staff:dashboard', pk=request.user.id)

    else: 
      form = LinkAccountForm()

  return render(request, 'staff/link_account.html', {'form': form})
