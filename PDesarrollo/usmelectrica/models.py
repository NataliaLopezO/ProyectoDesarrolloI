from django.db import models

id_type = (('C.C', 'C.C'),('C.E', 'C.E'),('NIT', 'NIT'),('Pasaporte', 'Pasaporte'))
type_cliente = (('Natural', 'Natural'),('Juridica', 'Juridica'))
payment_type = (('Presencial', 'Presencial'), ('Banco', 'Banco'), ('Virtual', 'Virtual'))
zone_type = (('Residencial', 'Residencial'), ('Comercial', 'Comercial'), ('Industrial', 'Industrial'))

# Create your models here.

class Administrador(models.Model):
    id_admin = models.IntegerField(primary_key= True)
    tipo_id_admin = models.CharField(max_length = 12, choices = id_type, default='C.C')
    celular_admin = models.IntegerField(null = True)
    nombre_admin = models.CharField(max_length = 64, null=True)
    email_admin = models.CharField(max_length = 64, null=True)
    direccion_admin = models.CharField(max_length = 64, null=True)
    contrasena_admin = models.CharField(max_length = 24, null=True)

class Operador(models.Model):
    id_operador = models.IntegerField(primary_key= True)
    tipo_id_operador = models.CharField(max_length = 12, choices = id_type, default='C.C')
    celular_operador = models.IntegerField(null = True)
    nombre_operador = models.CharField(max_length = 64, null=True)
    email_operador = models.CharField(max_length = 64, null=True)
    direccion_operador = models.CharField(max_length = 64, null=True)
    contrasena_operador = models.CharField(max_length = 24, null=True)
    estado_operador = models.BooleanField(default=True)

class Gerente(models.Model):
    id_gerente = models.IntegerField(primary_key= True)
    tipo_id_gerente = models.CharField(max_length = 12, choices = id_type, default='C.C')
    celular_gerente = models.IntegerField(null = True)
    nombre_gerente = models.CharField(max_length = 64, null=True)
    email_gerente = models.CharField(max_length = 64, null=True)
    direccion_gerente = models.CharField(max_length = 64, null=True)
    contrasena_gerente = models.CharField(max_length = 24, null=True)
    estado_gerente = models.BooleanField(default=True)


class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key= True)
    tipo_id_cliente = models.CharField(max_length = 12, choices = id_type, default='C.C')
    celular_cliente = models.IntegerField(null = True)
    nombre_cliente = models.CharField(max_length = 64, null=True)
    email_cliente = models.CharField(max_length = 64, null=True)
    direccion_cliente = models.CharField(max_length = 64, null=True)
    contrasena_cliente = models.CharField(max_length = 24, null=True)
    estado_cliente = models.BooleanField(default=True)
    tipo_cliente = models.CharField(max_length = 12, choices = id_type, default='Natural')
 
class Servicio(models.Model):
    cliente_id = models.ForeignKey(Cliente, null = False, blank = False, on_delete = models.CASCADE)
    tipo_servicios = models.CharField(max_length = 12, choices = zone_type, default='Residencial')
    estado_servicio = models.BooleanField(default = True)
    mora_servicio = models.BooleanField(default = False)

class Factura(models.Model):
    id_servicio = models.ForeignKey(Servicio, null = False, blank = False, on_delete = models.CASCADE)
    consumo_factura = models.IntegerField(null = False) #Podemos poner un consumo por defecto despues de realizar backend
    lectura_factura = models.IntegerField(null = False)
    total_factura = models.IntegerField(null = False)
    date_crea_factu = models.DateField(null = False)
    date_ven_factu = models.DateField(null = False)
    periodo_factu = models.DateField(null = False)

class Pago(models.Model):
    factura_id = models.ForeignKey(Factura, null = False, blank = False, on_delete = models.CASCADE)
    operador_id = models.ForeignKey(Operador, null = False, blank = False, on_delete = models.CASCADE)
    fecha_pago = models.DateField(null = False)
    forma_pago = models.CharField(max_length = 12, choices = payment_type, default = 'Presencial')
    total_pago = models.IntegerField(null = False)
