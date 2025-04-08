from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse
from .models import Medico , Consulta
from .forms import ConsultaForm

# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from .serializers import LivroSerializer


# Vizualizar medicos
def listar_medicos(request):
    medico = Medico.objects.all()
    return render(request, 'listar_medicos.html', {'medico' : medico})

# Criar consulta
def criar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form_consulta')
    else:
        form = ConsultaForm()
    return render(request, 'form_consulta.html' , {'form' : form})

#  detalhes consulta
def detalhes_consulta(request , pk):
    consulta = get_object_or_404(Consulta , pk=pk)
    return HttpResponse (f"Sua consulta: Paciente = {consulta.paciente} \n data = {consulta.data} \n medico = {consulta.medico}")


# Filtrar por especialidade

