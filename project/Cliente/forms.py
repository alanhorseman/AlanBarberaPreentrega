from django import forms
from . import models

class UsuariosForm(forms.ModelForm):
    pais_origen_id = forms.ModelChoiceField(queryset=models.Pais.objects.all(), widget=forms.Select(attrs={"class": "form-control"}))
    class Meta:
        model = models.Usuarios
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "required": "required"}),
            "pais_origen_id": forms.Select(attrs={"class": "form-control", "required": "required"})
        }