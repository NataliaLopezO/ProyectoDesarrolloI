from django.urls import path 
from . import views
from . import views_administrador

urlpatterns= [
    path('', views.loginApp, name='login'),

    ##url administrador
    path('administrador/', views_administrador.administrador, name='admin'),
    path('administrador/borrar_operador/<int:user_id>/', views_administrador.admin_borrar_operadores, name='admin_borrar_operadores'),
    path('administrador/borrar_gerente/<int:user_id>/', views_administrador.admin_borrar_gerentes, name='admin_borrar_gerentes'),
    path('administrador/crear/', views_administrador.admin_crear, name='admin_crear'),

    ##url gerente

    ##url operadores

    

    ##url clientes

   
]