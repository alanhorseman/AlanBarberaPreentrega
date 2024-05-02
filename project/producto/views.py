from django.shortcuts import render, redirect

from . import models, forms


def home(request):
    return render(request, "producto/index.html")

def productocategoria_list(request):
    consulta = request.GET.get("consulta", None)
    if consulta:
        query = models.ProductoCategoria.objects.filter(nombre__icontains=consulta)
    else:
        query = models.ProductoCategoria.objects.all()

    context = {"productos": query}
    return render(request, "producto/productocategoria_list.html", context)

def productocategoria_create(request):
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("producto:home")
    else:
        form = forms.ProductoCategoriaForm()
    return render(request, "producto/productocategoria_create.html", context={"form": form})

def productocategoria_detail(request, pk:int):
    query = models.ProductoCategoria.objects.get(id=pk)
    return render(request, "producto/productocategoria_detail.html", context={"producto": query})
