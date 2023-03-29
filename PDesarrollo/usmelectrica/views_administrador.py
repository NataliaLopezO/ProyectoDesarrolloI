from django.shortcuts import render, redirect
from .models import *
from .forms import editForm

#Para encriptar contrasenas
#Catualice models, viw_admin y view operador
from cryptography.fernet import Fernet
key=Fernet.generate_key()
objeto_cifrado=Fernet(key)


def administrador_inicio(request):
    return render(request, "social/administrador_inicio.html")

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
                        apellidoP_Gerente= request.POST['apellidoP'],
                        apellidoM_Gerente= request.POST['apellidoM'],
                        email_gerente= request.POST['email'],
                        direccion_gerente= request.POST['direccion'],
                        contrasena_gerente= objeto_cifrado.encrypt(str.encode(request.POST['contra'])))
            gerente.save()    

        ##crear operadores
        if(request.POST['tipousuario']=="operador"):
            operador = Operador(id_operador= int(request.POST['id']), 
                        tipo_id_operador= request.POST['tipoid'],  
                        celular_operador= int(request.POST['celular']), 
                        nombre_operador= request.POST['nombre'], 
                        apellidoP_Operador= request.POST['apellidoP'],
                        apellidoM_Operador= request.POST['apellidoM'],
                        email_operador= request.POST['email'],
                        direccion_operador= request.POST['direccion'],
                        contrasena_operador= objeto_cifrado.encrypt(str.encode(request.POST['contra'])))
            operador.save() 
  
        ##crear clientes

        if(request.POST['tipousuario']=="cliente"):
            cliente = Cliente(id_cliente= int(request.POST['id']), 
                        tipo_id_cliente= request.POST['tipoid'],  
                        celular_cliente= int(request.POST['celular']), 
                        nombre_cliente= request.POST['nombre'],
                        apellidoP_Cliente= request.POST['apellidoP'],
                        apellidoM_Cliente= request.POST['apellidoM'], 
                        email_cliente= request.POST['email'],
                        direccion_cliente= request.POST['direccion'],
                        contrasena_cliente= objeto_cifrado.encrypt(str.encode(request.POST['contra'])))
            cliente.save() 
    return 0

    
"""
def admin_actualizar_gerente1(request, user_id):
    form= editForm()
    
    return render(request, "social/actualizar_gerente.html", )

def admin_actualizar_gerente(request):
    form= editForm()
    return render(request, "social/actualizar_gerente.html",{'form':form} )

    
def admin_editar_gerente(request, user_id):
    if request.method =='POST' and request.id=='editar':
        ##Editar gerentes
        gerente= Gerente.objects.filter(id_gerente = user_id)
        gerente.update(celular_gerente= int(request.POST['celular_actualizar']))
        gerente.update(nombre_gerente= request.POST['nombre_actualizar'])
        gerente.update(email_gerente= request.POST['email_actualizar'])
        gerente.update(direccion_gerente= request.POST['direccion_actualizar'])
        gerente.update(contrasena_gerente= request.POST['contra_actualizar'])
        return redirect('admin')
    return render(request, "social/actualizar_gerente.html")

"""
def admin_actualizar_gerente1(request, user_id):
    gerente= Gerente.objects.filter(id_gerente = user_id)
    form= editForm(initial={'nombre':gerente.first().nombre_gerente, 'email':gerente.first().email_gerente, 
    'celular':gerente.first().celular_gerente, 'direccion':gerente.first().direccion_gerente, 'contraseña':gerente.first().contrasena_gerente,})
    if request.method =='POST':
        gerente.update(nombre_gerente= request.POST['nombre'])
        gerente.update(apellidoP_Gerente= request.POST['apellidoP'])
        gerente.update(apellidoM_Gerente= request.POST['apellidoM'])
        gerente.update(email_gerente= request.POST['email'])
        gerente.update(celular_gerente= int(request.POST['celular']))
        gerente.update(direccion_gerente= request.POST['direccion'])
        gerente.update(contrasena_gerente= objeto_cifrado.encrypt(str.encode(request.POST['contra'])))
        return redirect('admin')
    return render(request, "social/actualizar_gerente1.html", {'form':form})

def admin_actualizar_cliente(request, user_id):
    cliente= Cliente.objects.filter(id_cliente = user_id)
    form= editForm(initial={'nombre':cliente.first().nombre_cliente, 'email':cliente.first().email_cliente, 
    'celular':cliente.first().celular_cliente, 'direccion':cliente.first().direccion_cliente, 'contraseña':cliente.first().contrasena_cliente,})
    if request.method =='POST':
        cliente.update(nombre_cliente= request.POST['nombre'])
        cliente.update(apellidoP_Cliente= request.POST['apellidoP'])
        cliente.update(apellidoM_Cliente= request.POST['apellidoM'])
        cliente.update(email_cliente= request.POST['email'])
        cliente.update(celular_cliente= int(request.POST['celular']))
        cliente.update(direccion_cliente= request.POST['direccion'])
        cliente.update(contrasena_cliente= objeto_cifrado.encrypt(str.encode(request.POST['contra'])))
        return redirect('admin')
    return render(request, "social/actualizar_cliente.html", {'form':form})

def admin_actualizar_operador(request, user_id):
    operador= Operador.objects.filter(id_operador = user_id)
    form= editForm(initial={'nombre':operador.first().nombre_operador, 'email':operador.first().email_operador, 
    'celular':operador.first().celular_operador, 'direccion':operador.first().direccion_operador, 'contraseña':operador.first().contrasena_operador,})
    if request.method =='POST':
        operador.update(nombre_operador= request.POST['nombre'])
        operador.update(apellidoP_Operador= request.POST['apellidoP'])
        operador.update(apellidoM_Operador= request.POST['apellidoM'])
        operador.update(email_operador= request.POST['email'])
        operador.update(celular_operador= int(request.POST['celular']))
        operador.update(direccion_operador= request.POST['direccion'])
        operador.update(contrasena_operador= objeto_cifrado.encrypt(str.encode(request.POST['contra'])))
        return redirect('admin')
    return render(request, "social/actualizar_operador.html", {'form':form})


def admin_borrar_clientes(request, user_id):
    cliente= Cliente.objects.filter(id_cliente = user_id)
    estado = cliente.first().estado_cliente
    cliente.update(estado_cliente= (not estado))
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

def admin_borrar_clientes(request, user_id):
    cliente= Cliente.objects.filter(id_cliente = user_id)
    estado = cliente.first().estado_cliente
    cliente.update(estado_cliente= (not estado))
    return redirect('admin')

