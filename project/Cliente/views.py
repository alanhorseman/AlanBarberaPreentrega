from django.shortcuts import render
from . import views, models

# Create your views here.

def home(request):
    query = models.Usuarios.objects.all()
    context = {"usuarios": query}
    return render(request, "Cliente/index.html", context)

