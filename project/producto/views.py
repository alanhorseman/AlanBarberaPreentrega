from django.shortcuts import render

from . import models


def home(request):
    query = models.ProductoCategoria.objects.all()
    context = {"productos": query}
    return render(request, "producto/index.html", context)