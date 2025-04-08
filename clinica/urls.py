from django.urls import path
from . import views

urlpatterns = [
    path('medicos/', views.listar_medicos),
    path('consulta/nova', views.criar_consulta),#Para criar um novo item
    path('consultas/ <int:pk>', views.detalhes_consulta),#Modificar o item referenciado
]
