from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import Agendamento , Servico
from .serializers import ServicoSerializer , AgendamentoSerializer
from rest_framework import status


# Listar e postar serviços 
@api_view(['GET','POST'])
def read_servico(request):
    if request.method == "GET":
        try:
            servico = Servico.objects.all()
            serializer = ServicoSerializer(servico, many=True)
            return Response(serializer.data)
        
        except Servico.DoesNotExist:
            return Response({'erro': 'servico inexistentes'}, status= status.HTTP_400_BAD_REQUEST)
    
    if request.method == "POST":
        serializer = ServicoSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# listar e postar Agendamentos
@api_view(['GET','POST'])
def read_agendamento(request):
    if request.method == "GET":
        try:
            agendamento = Agendamento.objects.all()
            serializer = AgendamentoSerializer(agendamento, many=True)
            return Response(serializer.data)
        
        except Agendamento.DoesNotExist:
            return Response({'erro': 'agendamento inexistentes'}, status= status.HTTP_400_BAD_REQUEST)
    
    if request.method == "POST":
        serializer = AgendamentoSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



# Procurar servico com primary key
@api_view(['GET'])
def pegar_servico(request,pk):
    # utilizando try para possíveis erros do usuário
    try:
        servico = Servico.objects.get (pk=pk)
    # caso o 'Carro' não exista este erro irá aparecer   
    except Servico.DoesNotExist:
        return Response({'erro': 'Serviço inexistente'}, status= status.HTTP_404_NOT_FOUND)
    
    serializer =  ServicoSerializer(servico)
    return Response(serializer.data)

# Procurar agendamento com primary key
@api_view(['GET'])
def pegar_agendamento(request,pk):
    # utilizando try para possíveis erros do usuário
    try:
        servico = Agendamento.objects.get (pk=pk)
    # caso o 'Agendamento' não exista este erro irá aparecer   
    except Agendamento.DoesNotExist:
        return Response({'erro': 'Agendamento inexistente'}, status= status.HTTP_404_NOT_FOUND)
    
    serializer =  AgendamentoSerializer(servico)
    return Response(serializer.data)