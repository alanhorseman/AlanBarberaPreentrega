from django.shortcuts import render
from .forms import CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, CustomUserCreationForm

def home(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "code/index.html", {"mensaje": "Usuario creado"})
    else:
        form = CustomUserCreationForm()
    return render(request, "core/register.html", {"form": form})
