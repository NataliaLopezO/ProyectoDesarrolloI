from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def loginApp(request):
    if request.method =='POST':

        id = int(request.POST['user'])
        contra = request.POST['contra']
        ##Administrador
        if request.POST['tipousuario']=='admin':
            admin = Administrador.objects.filter(id_admin= id, contrasena_admin= contra)
            if admin.exists():
                return redirect('admin')
        ##Gerente
        if request.POST['tipousuario']=='gerente':
            gerente = Gerente.objects.filter(id_gerente= id, contrasena_gerente= contra)
            if gerente.exists():
                return redirect('gerente') 

        ##Operador
        if request.POST['tipousuario']=='operador':
            operador = Operador.objects.filter(id_operador= id, contrasena_operador= contra)
            if operador.exists():
                return redirect('operador') 
        

    return render(request, 'social/login.html')

