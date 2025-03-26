from django.shortcuts import render, redirect, get_object_or_404
from .models import Agendamento
from .forms import AgendamentoForm
from django.http import JsonResponse

def agenda(request):
    return render(request, 'agenda/agenda.html')

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

from django.http import JsonResponse
from .models import Agendamento

def listar_agendamentos_json(request):
    agendamentos = Agendamento.objects.all()
    eventos = []

    for agendamento in agendamentos:
        eventos.append({
            "title": f"{agendamento.nome} - {agendamento.servico}",
            "start": agendamento.data_agendamento.strftime("%d/%m/%Y %H:%M"),  # Formatação da data
            "end": agendamento.data_agendamento.strftime("%d/%m/%Y %H:%M"),  # Formatação da data
        })

    return JsonResponse(eventos, safe=False)

# View para excluir agendamento
def excluir_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)  # Buscar agendamento com o ID
    agendamento.delete()  # Excluir o agendamento
    return redirect('agenda')  # Redirecionar para a página de agenda
