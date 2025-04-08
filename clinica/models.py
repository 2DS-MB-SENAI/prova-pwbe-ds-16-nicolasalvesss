from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=255)
    PEDIATRA = 'Pediatra' , 'PD'
    FISIOTERAPEUTA =  'Fisioterapeuta' , 'FI'
    GINECOLOGISTA = 'Ginecologista' , 'GN'
    CARDIOLOGISTA = 'CAR' , 'Cardiologista'
    especialidades_choices = [
        ('PEDIATRA', 'Pediatra'),
        ('FISIOTERAPEUTA', 'Fisioterapeuta'),
        ('GINECOLOGISTA', 'Ginecologista'),
        ('CARDIOLOGISTA' , 'Cardiologista'),
        ('CAR' , 'Car'),
    ]
    especialidade = models.CharField(max_length=50 , choices=especialidades_choices)
    crm = models.CharField(max_length=255, unique= True ) #Não esquecer de formatar da maneira correta
    email = models.EmailField()
    def __str__(self):
        return self.nome
    
class Consulta(models.Model):
    paciente = models.CharField(max_length=255)
    data = models.DateTimeField()
    medico =models.ForeignKey(Medico, on_delete=models.CASCADE)
    AGENDADO = 'Agendado'
    REALIZADO = 'Realizado'
    CANCELADO = 'Cancelado'
    status_choices = [
        (AGENDADO , 'Agendado'),
        (REALIZADO , 'Realizado'),
        (CANCELADO , 'Cancelado'),
    ]
    status = models.CharField(max_length=9 , choices=status_choices)
    detalhes = models.CharField(max_length=255)
    
    def __str__(self):
        return self.paciente