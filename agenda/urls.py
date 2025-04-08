from . import views
from django.urls import path
# As urls do projeto

urlpatterns = [
    path('api/servicos/', views.read_servico ),
    path('api/agendamentos/', views.read_agendamento),
    path('api/servico/<int:pk>', views.pegar_servico),
    path('api/agendamentos/<int:pk>', views.pegar_agendamento),
]
