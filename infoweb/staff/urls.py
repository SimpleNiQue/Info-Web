from django.urls import path
from . import views


app_name = 'staff'
urlpatterns = [
    path('', views.index, name='home'),
    path('dashboard/<str:pk>/', views.dashboard, name='dashboard'),
    path('link-account/', views.link_account, name='link_account'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login' ),
    path('logout/', views.log_out, name='logout'),
]