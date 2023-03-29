from django.shortcuts import render, redirect
from .models import *
from .forms import editForm

def gerente(request):
    clientes = Cliente.objects.all()
    operadores = Operador.objects.all()
    administradores = Administrador.objects.all()
    
    return render(request, "social/gerente.html", {'clientes': clientes, 'operadores':operadores,'administradores':administradores })