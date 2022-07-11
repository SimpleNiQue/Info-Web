from django.urls import path
from . import views


app_name = 'staff'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('dashboard/<str:pk>/', views.dashboard, name='dashboard'),
    path('link-account/<str:pk>/', views.link_account, name='link_account'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login' ),
    path('logout/', views.log_out, name='logout'),
]