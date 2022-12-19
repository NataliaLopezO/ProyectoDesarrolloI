from django.shortcuts import render, redirect
from .models import *


def administrador(request):
    gerentes = Gerente.objects.all()
    operadores = Operador.objects.all()
    clientes = Cliente.objects.all()
    
    return render(request, "social/administrador.html", {'gerentes': gerentes, 'operadores':operadores,'clientes':clientes })

def admin_crear(request):
    if request.method =='POST':
        ##crear gerentes
        if(request.POST['tipousuario']=="gerente"):
            gerente = Gerente(id_gerente= int(request.POST['id']), 
                        tipo_id_gerente= request.POST['tipoid'],  
                        celular_gerente= int(request.POST['celular']), 
                        nombre_gerente= request.POST['nombre'], 
                        email_gerente= request.POST['email'],
                        direccion_gerente= request.POST['direccion'],
                        contrasena_gerente= request.POST['contra'])
            gerente.save()    
        ##crear operadores
        if(request.POST['tipousuario']=="operador"):
            operador = Operador(id_operador= int(request.POST['id']), 
                        tipo_id_operador= request.POST['tipoid'],  
                        celular_operador= int(request.POST['celular']), 
                        nombre_operador= request.POST['nombre'], 
                        email_operador= request.POST['email'],
                        direccion_operador= request.POST['direccion'],
                        contrasena_operador= request.POST['contra'])
            operador.save() 

        ##crear clientes


    return render(request, "social/registro.html")
    

def admin_actualizar(request, user_id):
    return redirect('admin')

def admin_borrar_operadores(request, user_id):
    operador = Operador.objects.filter(id_operador = user_id)
    estado = operador.first().estado_operador
    operador.update(estado_operador= (not estado))
    return redirect('admin')

def admin_borrar_gerentes(request, user_id):
    gerente= Gerente.objects.filter(id_gerente = user_id)
    estado = gerente.first().estado_gerente
    gerente.update(estado_gerente= (not estado))
    return redirect('admin')

