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

#se agrego lo de abajo
class UsuariosList(ListView):
    model = models.Usuarios
    template_name = 'cliente/usuarios_list.html'  
    context_object_name = 'usuarios'  

    def get_queryset(self):
        queryset = super().get_queryset()  

        # Obtiene la consulta de la URL
        consulta = self.request.GET.get('consulta')

        if consulta:
            queryset = queryset.filter(nombre__icontains=consulta)

        return queryset