from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse
from .models import Medico , Consulta
from .forms import ConsultaForm
from datetime import datetime, timedelta


# Vizualizar medicos
def listar_medicos(request):
    medicos = Medico.objects.all()
    especialidade = request.GET.get('especialidade')  
    if especialidade:
        medico = Medico.objects.filter(especialidade__icontains=especialidade) 
        return render(request, 'listar_medicos.html', {'medico' : medico})
    else:
        medico = Medico.objects.all()
    return render(request, 'listar_medicos.html', {'medicos' : medicos})

# Criar consulta
def criar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form_consulta')
        else:
            return render(request)
    else:
        form = ConsultaForm()
    return render(request, 'form_consulta.html' , {'form' : form})

#  detalhes consulta
def detalhes_consulta(request , pk):
    consulta = get_object_or_404(Consulta , pk=pk)
    return HttpResponse (f"Sua consulta: Paciente = {consulta.paciente} \n data = {consulta.data} \n medico = {consulta.medico}")


