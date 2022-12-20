from django.urls import path 
from . import views
from . import views_administrador, views_gerente, views_operador

urlpatterns= [
    path('', views.loginApp, name='login'),

    ##url administrador
    path('administrador/', views_administrador.administrador, name='admin'),
    path('administrador/borrar_operador/<int:user_id>/', views_administrador.admin_borrar_operadores, name='admin_borrar_operadores'),
    path('administrador/borrar_gerente/<int:user_id>/', views_administrador.admin_borrar_gerentes, name='admin_borrar_gerentes'),
    path('administrador/borrar_cliente/<int:user_id>/', views_administrador.admin_borrar_clientes, name='admin_borrar_clientes'),
    path('administrador/crear/', views_administrador.admin_crear, name='admin_crear'),
    path('administrador/actualizar_gerente/<int:user_id>/', views_administrador.admin_actualizar_gerente1, name='admin_actualizar_gerente1'),
    path('administrador/actualizar_cliente/<int:user_id>/', views_administrador.admin_actualizar_cliente, name='admin_actualizar_cliente'),
    path('administrador/actualizar_operador/<int:user_id>/', views_administrador.admin_actualizar_operador, name='admin_actualizar_operador'),
    ##url gerente
    path('gerente/', views_gerente.gerente, name='gerente'),

    ##url operadores
    path('operador/', views_operador.operador, name='operador'),
    path('operador/borrar_cliente/<int:user_id>/', views_operador.operador_borrar_clientes, name='operador_borrar_clientes'),
    path('operador/crear/', views_operador.crear, name='operador_crear'),
    path('operador/actualizar_cliente/<int:user_id>/', views_operador.operador_actualizar_cliente, name='operador_actualizar_cliente'),
    

    ##url clientes
]