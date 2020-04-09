from django.urls import path
from ip_info import views

urlpatterns = [
    path('', views.home, name='home'),
]
