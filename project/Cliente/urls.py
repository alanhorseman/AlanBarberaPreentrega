from django.urls import path
from . import views
# from django.

app_name = "Cliente"

urlpatterns = [
    path('home/', views.home),
]