from django.urls import path
from . import views
# from django.

app_name = "cliente"

urlpatterns = [
    path('home/', views.home, name="home"),
    path("usuarios/create/", views.UsuariosCreate.as_view(), name="usuarios_create"),
    path("usuarios/list/", views.UsuariosList.as_view(), name="usuarios_list"), #
]