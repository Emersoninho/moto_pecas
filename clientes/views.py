from django.shortcuts import render

def clientes(request):
    if request.method == 'GET':
        return render(request, 'clientes/clientes.html')
    elif request.method == 'POST':
        name = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carros = request.POST.getlist('carro')
        placas = request.POST.getlist('placa')
        anos = request.POST.getlist('ano')
