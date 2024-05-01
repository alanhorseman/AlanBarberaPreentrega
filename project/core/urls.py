from django.urls import path
from . import views
# from django.

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
]