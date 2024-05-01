from django.urls import path
from . import views
# from django.

app_name = "producto"

urlpatterns = [
    path('home/', views.home, name="home"),
]