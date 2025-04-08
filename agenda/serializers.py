from .models import Agendamento , Servico
from rest_framework import serializers 

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        # pegando dos itens do models e transformando em json 
        model = Servico
        fields = "__all__"

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        # pegando dos itens do models e transformando em json 
        model = Agendamento
        fields = "__all__"
