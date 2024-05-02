from django.urls import path
from . import views
# from django.

app_name = "producto"

urlpatterns = [
    path('home/', views.home, name="home"),
    path("productocategoria/create/", views.ProductoCategoriaCreate.as_view(), name="productocategoria_create"),
    path("productocategoria/list/", views.ProductoCategoriaList.as_view(), name="productocategoria_list"),
    path("productocategoria/detail/<int:pk>", views.ProductoCategoriaDetail.as_view(), name="productocategoria_detail"),
    path("productocategoria/update/<int:pk>", views.ProductoCategoriaUpdate.as_view(), name="productocategoria_update"),
    path("productocategoria/delete/<int:pk>", views.ProductoCategoriaDelete.as_view(), name="productocategoria_delete"),
]