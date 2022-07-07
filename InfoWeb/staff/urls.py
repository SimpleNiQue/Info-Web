from django.urls import path
from .views import IndexView, dashboard,add_user_profile ,login_user, register, log_out


app_name = 'staff'
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('dashboard/<str:pk>/', dashboard, name='dashboard'),
    path('add-user-profile/<str:user>/', add_user_profile, name='add_user_profile'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login' ),
    path('logout/', log_out, name='logout'),
]