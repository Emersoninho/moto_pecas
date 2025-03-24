from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Cliente, Carro  # Certifique-se de importar corretamente
import re
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Cliente, Carro
import re
import json
from django.core import serializers
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

        # 🚨 Validação de CPF e E-mail antes de cadastrar
        if Cliente.objects.filter(cpf=cpf).exists():
            return render(request, 'clientes/clientes.html', {
                'erro': 'CPF já cadastrado!',
                'nome': nome, 'sobrenome': sobrenome, 'email': email, 'carros': zip(carros, placas, anos)
            })

        if Cliente.objects.filter(email=email).exists():
            return render(request, 'clientes/clientes.html', {
                'erro': 'E-mail já cadastrado!',
                'nome': nome, 'sobrenome': sobrenome, 'cpf': cpf, 'carros': zip(carros, placas, anos)
            })

        # 🚨 Validação de formato de e-mail
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email):
            return render(request, 'clientes/clientes.html', {
                'erro': 'E-mail inválido!',
                'nome': nome, 'sobrenome': sobrenome, 'cpf': cpf, 'carros': zip(carros, placas, anos)
            })

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
            car = Carro(carro=carro, placa=placa, ano=ano, cliente=cliente)
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
        cliente.nome = nome
        cliente.sobrenome = sobrenome
        cliente.email = email
        cliente.cpf = cpf
        cliente.save()
        return JsonResponse({'status': '200', 'nome': nome, 'sobrenome': sobrenome, 'email': email, 'cpf': cpf})
    except:
        return JsonResponse({'status': '500'})