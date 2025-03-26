from django.urls import path
from . import views

urlpatterns = [
    path('', views.agenda, name='agenda'),
    path('novo/', views.criar_agendamento, name='criar_agendamento'),
    path('listar/', views.listar_agendamentos, name='listar_agendamentos'),
    path('json/', views.listar_agendamentos_json, name='listar_agendamento_json'),
    path('excluir/<int:id>/', views.excluir_agendamento, name='excluir_agendamento'), 
]

