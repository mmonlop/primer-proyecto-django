from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.principal,name='principal'),
    path('ji', views.ji, name='ji'),
    path('<int:pk>', views.detalle_post, name='detalle'),
    path('autores/', views.autores_listado,name='autores')
]