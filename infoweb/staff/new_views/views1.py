# #* Django imports
# from django.shortcuts import render, redirect, get_object_or_404
# from django.urls import reverse_lazy
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.models import Group        

# # My imports
# from .models import LinkedAccount, PersonalDetails, WorkDetails
# from .forms import LinkAccountForm, PersonalDetails, CreateUserForm

# #==============================================================

# class IndexView(LoginRequiredMixin, View):
#     login_url = '/staff/login/'
#     redirect_field_name = 'redirect_to'

#     def get(self, request, *args, **kwargs):
#         context = {}
#         return render(request, 'staff/index.html', context)


# class LoginUserView(View):
#     def post(self, request, *args, **kwargs):
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             login(request, user)
#             return redirect('staff:dashboard', pk=str(request.user.id))
        
#         else: 
#             messages.error(request, 'Account not Registered')
#             return render(request, 'staff/login.html')
    
#     def get(self, request, *args, **kwargs):
#         return render(request, 'staff/login.html')


# class LogOutView(LoginRequiredMixin, View):
#     login_url = '/staff/login/'
#     redirect_field_name = 'redirect_to'

#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return redirect('staff:home')


# class RegisterView(View):
#     def post(self, request, *args, **kwargs):
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request," Account was Created for "+username)
#             return redirect('staff:login')
#         else:
#             messages.error(request, 'Incorrect credentials')
#             return render(request, 'staff/register.html', {'form': form})
    
#     def get(self, request, *args, **kwargs):
#         form = CreateUserForm()
#         return render(request, 'staff/register.html', {'form': form})


# class DashboardView(LoginRequiredMixin, View):
#     login_url = '/staff/login/'
#     redirect_field_name = 'redirect_to'

#     def get(self, request, *args, **kwargs):
#         context = {}
#         pk = kwargs.get('pk')
        
#         if str(request.user.id) == str(pk):
#             try:
#                 work = WorkDetails.objects.get(user=pk)
#                 context['work'] = work
#             except Exception as error:
#                 print(f"{error
