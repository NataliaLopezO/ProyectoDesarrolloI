from django import forms

class editForm (forms.Form):
    nombre= forms.CharField(label="Nombre", required=True)
    email= forms.CharField(label="Email",  required=True)
    celular= forms.IntegerField(label="Celular", required=True)
    direccion= forms.CharField(label="Direccion", required=True)
    contraseña= forms.CharField(label="Contraseña", widget=forms.PasswordInput,required=False)