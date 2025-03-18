from django.shortcuts import render
from .models import Cliente, Carro  # Certifique-se de importar corretamente
import re

def clientes(request):
    if request.method == 'GET':
        return render(request, 'clientes/clientes.html')

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
