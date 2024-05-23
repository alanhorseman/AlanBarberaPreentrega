from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import models, forms

def home(request):
    return render(request, "producto/index.html")

class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria
    template_name = 'producto/productocategoria_list.html'  
    context_object_name = 'categorias'  

    def get_queryset(self):
        queryset = super().get_queryset()  

        # Obtiene la consulta de la URL
        consulta = self.request.GET.get('consulta')

        if consulta:
            queryset = queryset.filter(nombre__icontains=consulta)

        return queryset

class ProductoCategoriaCreate(LoginRequiredMixin, CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:home")

class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria

class ProductoCategoriaUpdate(LoginRequiredMixin, UpdateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")
    
    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)

class ProductoCategoriaDelete(LoginRequiredMixin, DeleteView):
    model = models.ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")
