from django.shortcuts import render
from . import views
 
def home(request):
    return render(request, "core/index.html")