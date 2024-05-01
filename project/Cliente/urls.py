from django.urls import path
from . import views
# from django.

app_name = "cliente"

urlpatterns = [
    path('home/', views.home, name="home"),
]