from django.shortcuts import render, redirect
from .models import Agendamento
from .forms import AgendamentoForm

def agenda(request):
    return render(request, 'agenda.html')

# Página para criar um agendamento
def criar_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_agendamentos')  # Redireciona para a lista
    else:
        form = AgendamentoForm()

    return render(request, 'agenda/criar_agendamento.html', {'form': form})

# Página para listar os agendamentos
def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'agenda/listar_agendamentos.html', {'agendamentos': agendamentos})
