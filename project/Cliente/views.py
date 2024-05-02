from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models, forms

# Create your views here.

def home(request):
    query = models.Usuarios.objects.all()
    context = {"usuarios": query}
    return render(request, "cliente/index.html", context)

class UsuariosCreate(CreateView):
    model = models.Usuarios
    form_class = forms.UsuariosForm
    success_url = reverse_lazy("cliente:home")
