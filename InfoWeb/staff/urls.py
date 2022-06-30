from django.urls import path
from .views import index, nominal_roll


app_name = 'staff'
urlpatterns = [
    path('', index, name='home'),
    path('nominal-roll/<str:pk>/', nominal_roll, name='norminal_roll')
]