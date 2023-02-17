# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.shortcuts import render, redirect, HttpResponse
# from django.views import View

# from staff.forms import LinkAccountForm
# from staff.models import WorkDetails, LinkedAccount

# class DashboardView(View):
#     def get(self, request, pk):
#         context = {}
#         if str(request.user.id) == str(pk):
#             try:
#                 work = WorkDetails.objects.get(user=pk)
#                 context['work'] = work
#             except Exception as error:
#                 print(f"{error=}")
#                 return redirect('staff:link_account')
#         else:
#             print(f'Please Login First, request.user:{request.user}, pk:{pk}')
#             return HttpResponse("Please Login First")
#         return render(request, 'staff/dashboard.html', context)

# class LinkAccountView(View):
#     def get(self, request):
#         available_linked_users = [str(name) for name in LinkedAccount.objects.all()]

#         if str(request.user) in available_linked_users:
#             return redirect('staff:dashboard', pk=request.user.id)
#         else:
#             form = LinkAccountForm()

#         return render(request, 'staff/link_account.html', {'form': form})

#     def post(self, request):
#         available_linked_users = [str(name) for name in LinkedAccount.objects.all()]

#         if str(request.user) in available_linked_users:
#             return redirect('staff:dashboard', pk=request.user.id)

#         form = LinkAccountForm(request.POST)
#         if form.is_valid():
#             collected_user_id = form.cleaned_data['id_number']
#             collected_first_name = form.cleaned_data['first_name']

#             try:
#                 work_details = WorkDetails.objects.get(user=request.user)
#                 ID, FILE = (work_details.ID_number, work_details.personal_detail.first_name,)
#             except AttributeError as err:
#                 messages.error(request, "such User does not exist")
#                 print(f"{err=}")
#             else:
#                 if (ID == collected_user_id and FILE == collected_first_name):
#                     form.save(request.user)
#                     print("\nNew User Added/Linked")
#                     return redirect('staff:dashboard', pk=request.user.id, user=request.user)
#                 else:
#                     messages.error(request, "Invalid Credentials !!!")
#         return render(request, 'staff/link_account.html', {'form': form})
