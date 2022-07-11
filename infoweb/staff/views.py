#* Django imports
from typing import Optional
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



class IndexView(ListView):
    template_name: str = 'staff/index.html'
    context_object_name: Optional[str] = 'personal_details'

    def get_queryset(self):
        return PersonalDetails.objects.all()


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
def dashboard(request, pk):
  context: dict = {}

  try:
    personal = LinkedAccount.objects.get(id=pk)
    context['personal'] = personal
    
  except Exception as error:
    print(f"{error=}")
    return redirect('staff:link_account', pk=pk)
  
  return render(request, 'staff/dashboard.html', context)



@login_required(login_url='staff:login')
def link_account(request, pk):
  
  # if this is a POST request we need to process the form data
  if request.method == 'POST':
    # create a form instance and populate it with data from the request:
    form = LinkAccountForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
      # process the data in form.cleaned_data as required
      # ...

      # Get the data from the form
      user = request.user.username
      user_id = form.cleaned_data['ID_number']
      file_number = form.cleaned_data['file_number']

      #Check if the data corresponds from the database
      
      try:
        person_details = PersonalDetails.objects.get(ID_number=user_id)

        ID, FILE = (person_details.ID_number,person_details.ID_number.file_number,)

      except AttributeError as err:
        messages.error(request, "such User does not exist")
        print(f"{err=}")

      else:
  
        if (ID==user_id and FILE==file_number):
          form.save()
          print("\nNew User Added/Linked")
          return redirect('staff:dashboard', pk=pk) 
        else:
          # If none matches
          messages.error(request, "Invalid Credentials !!!")
 

  # if a GET (or any other method) we'll create a blank form
  else:
      form = LinkAccountForm()

  return render(request, 'staff/link_account.html', {'form': form})
