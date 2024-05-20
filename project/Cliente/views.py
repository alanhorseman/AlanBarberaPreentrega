from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models, forms
from .models import Pais
from .forms import UsuariosForm, PaisForm
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    query = models.Usuarios.objects.all()
    context = {"usuarios": query}
    return render(request, "cliente/index.html", context)

def usuarios_form(request):
    if request.method == "POST":
        form = UsuariosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = UsuariosForm()

    nuevo_pais_id = request.GET.get('pais_id')
    if nuevo_pais_id:
        form.fields['pais_origen_id'].queryset = Pais.objects.all()
        form.initial['pais_origen_id'] = nuevo_pais_id

    return render(request, 'usuarios_form.html', {'form': form})

def agregar_pais(request):
    if request.method == "POST":
        form = PaisForm(request.POST)
        if form.is_valid():
            nuevo_pais = form.save()
            # Utiliza el success_url definido en UsuariosCreate para redirigir
            return HttpResponseRedirect(reverse_lazy('cliente:usuarios_create'))
    else:
        form = PaisForm()
    return render(request, 'cliente/agregar_pais.html', {'form': form})

def eliminar_pais(request, pk):
    # Obtén el país que se va a eliminar
    pais = get_object_or_404(Pais, pk=pk)
    # Elimina el país
    pais.delete()
    # Redirecciona a donde desees después de eliminar el país
    return redirect('cliente:home')

class UsuariosCreate(CreateView):
    model = models.Usuarios
    form_class = forms.UsuariosForm
    success_url = reverse_lazy("cliente:home")

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

class UsuariosUpdate(UpdateView):
    model = models.Usuarios
    form_class = forms.UsuariosForm
    success_url = reverse_lazy("cliente:usuarios_list")

class UsuariosDelete(DeleteView):
    model = models.Usuarios
    success_url = reverse_lazy("cliente:usuarios_list")