from django.urls import path
from .views import IndexView, DashboardView ,login_user, register, log_out


app_name = 'staff'
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('dashboard/<str:pk>/', DashboardView.as_view(), name='dashboard'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login' ),
    path('logout/', log_out, name='logout'),
]