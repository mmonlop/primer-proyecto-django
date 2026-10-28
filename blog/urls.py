from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.principal,name='principal'),
    path('ji', views.ji, name='ji') 
]