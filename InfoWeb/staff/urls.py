from django.urls import path
from .views import IndexView, login_user, register, log_out


app_name = 'staff'
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login' ),
    path('logout/', log_out, name='logout'),
]