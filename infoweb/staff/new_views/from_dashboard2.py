# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.shortcuts import render, redirect, HttpResponse
# from django.views.generic import TemplateView, FormView

# from .models import WorkDetails, LinkedAccount
# from .forms import LinkAccountForm

# class DashboardView(TemplateView):
#     template_name = 'staff/dashboard.html'

#     @login_required(login_url='staff:login')
#     def dispatch(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         if str(request.user.id) != str(pk):
#             print(f'Please Login First, request.user:{request.user}, pk:{pk}')
#             return HttpResponse("Please Login First")
#         try:
#             work = WorkDetails.objects.get(user=pk)
#             self.context = {'work': work}
#         except Exception as error:
#             print(f"{error=}")
#             return redirect('staff:link_account')
#         return super().dispatch(request, *args, **kwargs)

# class LinkAccountView(FormView):
#     form_class = LinkAccountForm
#     template_name = 'staff/link_account.html'
#     success_url = '/'

#     @login_required(login_url='staff:login')
#     def dispatch(self, request, *args, **kwargs):
#         available_linked_users = [str(name) for name in LinkedAccount.objects.all()]
#         if str(request.user) in available_linked_users:
#             return redirect('staff:dashboard', pk=request.user.id)
#         return super().dispatch(request, *args, **kwargs)

#     def form_valid(self, form):
#         collected_user_id = form.cleaned_data['id_number']
#         collected_first_name = form.cleaned_data['first_name']

#         try:
#             work_details = WorkDetails.objects.get(user=self.request.user)
#             ID, FILE = (work_details.ID_number, work_details.personal_detail.first_name)
#         except AttributeError as err:
#             messages.error(self.request, "Such User Does Not Exist")
#             print(f"{err=}")
#         else:
#             if (ID == collected_user_id and FILE == collected_first_name):
#                 form.save(self.request.user)
#                 print("\nNew User Added/Linked")
#                 return redirect('staff:dashboard', pk=self.request.user.id) 
#             else:
#                 messages.error(self.request, "Invalid Credentials")
#         return super().form_valid(form)
