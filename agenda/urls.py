from django.urls import path
from . import views

urlpatterns = [
    path('', views.agenda, name='agenda'),
     path('novo/', views.criar_agendamento, name='criar_agendamento'),
    path('listar/', views.listar_agendamentos, name='listar_agendamentos'),
]

