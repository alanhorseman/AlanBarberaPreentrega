from django import forms
from . import models
from .models import Pais

class UsuariosForm(forms.ModelForm):
    pais_origen_id = forms.ModelChoiceField(
        queryset=models.Pais.objects.all(),
        label="País",
        widget=forms.Select(attrs={"class": "form-control"}))
    
    tarjeta_id = forms.ModelChoiceField(
        queryset=models.MetodosPagos.objects.all(),
        label="Metodo de pago",
        widget=forms.Select(attrs={"class": "form-control"}))
    
    class Meta:
        model = models.Usuarios
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "pais_origen_id": forms.Select(attrs={"class": "form-control", "required": "required"}),
            "tarjeta_id": forms.TextInput(attrs={"class": "form-control"}),
        }

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }