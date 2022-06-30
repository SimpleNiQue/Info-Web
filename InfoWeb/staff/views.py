#* Django imports
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
#====================================================

# My imports
from .models import PersonalDetails
from .forms import PersonalDetails, CreateUserForm, WorkDetails
from .decorators import allowed_users, unauthenticated_user
#==============================================================


def index(request):
    personal_details = PersonalDetails.objects.all()
    
    context = {
        'personal_details': personal_details
    }
    return render(request, 'staff/index.html', context)

def nominal_roll(request, pk):

    personal_details = PersonalDetails.objects.get(ID_number=pk)

    context = {
        'personal_details': personal_details
    }

    return render(request, 'staff/nominal_roll.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.info(request, "Username or Password is incorrect!")

    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUSer(request):
    logout(request)
    return redirect('login')