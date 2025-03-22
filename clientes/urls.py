from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes, name='clientes'),
    path('atualiza_cliente/', views.att_cliente, name='atualizar_cliente'),
    path('update_carro/<int:id>/', views.update_carro, name='update_carro'),
]
