from django.shortcuts import render, redirect

from . import models, forms


def home(request):
    if request.GET["consulta"]:
        consulta = request.GET["consulta"]
        query = models.ProductoCategoria.objects.filter(nombre__icontains=consulta)
    else:
        query = models.ProductoCategoria.objects.all()
    context = {"productos": query}
    return render(request, "producto/index.html", context)

def productocategoria_create(request):
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("producto:home")
    else:
        form = forms.ProductoCategoriaForm()
    return render(request, "producto/productocategoria_create.html", context={"form": form})

