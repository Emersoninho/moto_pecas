from django.db import models

class Agendamento(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    servico = models.CharField(max_length=100)
    data_agendamento = models.DateTimeField()

    def __str__(self):
        return f"{self.nome} - {self.servico} ({self.data_agendamento.strftime('%d/%m/%Y %H:%M')})"
