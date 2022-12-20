from django.shortcuts import render, redirect
from .models import *
from .forms import editForm


def operador(request):
    clientes = Cliente.objects.all()
    
    return render(request, "social/operador.html", {'clientes':clientes })

def crear (request):
    if request.method =='POST':
        ##crear clientes
        if(request.POST['tipousuario']=="cliente"):
            cliente = Cliente(id_cliente= int(request.POST['id']), 
                        tipo_id_cliente= request.POST['tipoid'],  
                        celular_cliente= int(request.POST['celular']), 
                        nombre_cliente= request.POST['nombre'], 
                        email_cliente= request.POST['email'],
                        direccion_cliente= request.POST['direccion'],
                        contrasena_cliente= request.POST['contra'])
            cliente.save() 

    return render(request, "social/registro.html")

def operador_borrar_clientes(request, user_id):
    cliente= Cliente.objects.filter(id_cliente = user_id)
    estado = cliente.first().estado_cliente
    cliente.update(estado_cliente= (not estado))
    return redirect('operador')

def operador_actualizar_cliente(request, user_id):
    cliente= Cliente.objects.filter(id_cliente = user_id)
    form= editForm(initial={'nombre':cliente.first().nombre_cliente, 'email':cliente.first().email_cliente, 
    'celular':cliente.first().celular_cliente, 'direccion':cliente.first().direccion_cliente, 'contraseña':cliente.first().contrasena_cliente,})
    if request.method =='POST':
        cliente.update(nombre_cliente= request.POST['nombre'])
        cliente.update(email_cliente= request.POST['email'])
        cliente.update(celular_cliente= int(request.POST['celular']))
        cliente.update(direccion_cliente= request.POST['direccion'])
        cliente.update(contrasena_cliente= request.POST['contraseña'])
        return redirect('operador')
    return render(request, "social/actualizar_cliente.html", {'form':form})