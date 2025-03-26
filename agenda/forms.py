from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['nome', 'telefone', 'servico', 'data_agendamento']
        widgets = {
            'data_agendamento': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
