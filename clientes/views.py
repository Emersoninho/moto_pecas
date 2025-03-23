from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Cliente, Carro  # Certifique-se de importar corretamente
import re
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

def clientes(request):
    if request.method == 'GET':
        clientes_list = Cliente.objects.all()
        return render(request, 'clientes/clientes.html', {'clientes': clientes_list})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carros = request.POST.getlist('carro')
        placas = request.POST.getlist('placa')
        anos = request.POST.getlist('ano')

        cliente = Cliente.objects.filter(cpf=cpf)
        if cliente.exists():
            return render(request, 'clientes/clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'carro': zip(carros, placas, anos)})

        # Validação de email
        if not re.fullmatch(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email):
            return render(request, 'clientes/clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'cpf': cpf, 'carros': zip(carros, placas, anos)})

        # Criar cliente
        cliente = Cliente(
            nome=nome,
            sobrenome=sobrenome,
            email=email,
            cpf=cpf
        )
        cliente.save()

        # Criar carros associados ao cliente
        for carro, placa, ano in zip(carros, placas, anos):
            car = Carro(carro=carro, placa=placa, ano=ano, cliente=cliente)  # Usando Carro (com C maiúsculo)
            car.save()

        return render(request, 'clientes/clientes.html', {'mensagem': 'Cliente cadastrado com sucesso!'})

def att_cliente(request):
    id_cliente = request.POST.get('id_cliente')
    cliente = Cliente.objects.filter(id=id_cliente)
    carros = Carro.objects.filter(cliente=cliente[0])
    cliente_id = json.loads(serializers.serialize('json', cliente))[0]['pk']
    clientes_json = json.loads(serializers.serialize('json', cliente))[0]['fields']
    carros_json = json.loads(serializers.serialize('json', carros))
    carros_json = [{'fields': carro['fields'], 'id': carro['pk']} for carro in carros_json]
    data = {'cliente': clientes_json, 'carros': carros_json, 'cliente_id': cliente_id}
    return JsonResponse(data)

@csrf_exempt
def update_carro(request, id):
    nome_carro = request.POST.get('carro')
    placa = request.POST.get('placa')
    ano = request.POST.get('ano')

    try:
        carro = Carro.objects.get(id=id)
        list_carro = Carro.objects.filter(placa=placa).exclude(id=id)
        if list_carro.exists():
            return JsonResponse({'mensagem': 'Placa já existe'})
        carro.carro = nome_carro
        carro.placa = placa
        carro.ano = ano
        carro.save()
        return JsonResponse({'mensagem': 'Dados alterados com sucesso!'})
    except Carro.DoesNotExist:
        return JsonResponse({'mensagem': 'Carro não encontrado'})
    
def excluir_carro(request, id):
    try:
        carro = Carro.objects.get(id=id)
        carro.delete()
        return redirect(reverse('clientes')+f'?aba=att_cliente&id_cliente={id}')
    except:
        return redirect(reverse('clientes')+f'?aba=att_cliente&id_cliente={id}')
    
def update_cliente(request, id):
    body = json.loads(request.body)
    nome = body['nome']
    sobrenome = body['sobrenome']
    email = body['email']
    cpf = body['cpf']

    cliente = get_object_or_404(Cliente, id=id)
    try:
        cliente = Cliente.objects.get(id=id)
        email_cliente = Cliente.objects.filter(email=email).exclude(id=id)
        if email_cliente.exists():
            return JsonResponse({'mensagem': 'email já existe'})
        cpf_cliente = Cliente.objects.filter(cpf=cpf).exclude(id=id)
        if cpf_cliente.exists():
            return JsonResponse({'mensagem': 'cpf ja existe'})
        
        cliente.nome = nome
        cliente.sobrenome = sobrenome
        cliente.email = email
        cliente.cpf = cpf
        cliente.save()
        return JsonResponse({'status': '200', 'nome': nome, 'sobrenome': sobrenome, 'email': email, 'cpf': cpf})
    except:
        return JsonResponse({'status': '500'})