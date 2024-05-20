from django.urls import path
from . import views
# from django.

app_name = "cliente"

urlpatterns = [
    path('home/', views.home, name="home"),
    path("usuarios/create/", views.UsuariosCreate.as_view(), name="usuarios_create"),
    path("usuarios/list/", views.UsuariosList.as_view(), name="usuarios_list"),
    path("usuarios/update/<int:pk>", views.UsuariosUpdate.as_view(), name="usuarios_update"),
    path("usuarios/delete/<int:pk>", views.UsuariosDelete.as_view(), name="usuarios_delete"),
    path("agregar_pais/", views.agregar_pais, name="agregar_pais"),
    path("pais/<int:pk>/eliminar/", views.eliminar_pais, name="eliminar_pais")
]