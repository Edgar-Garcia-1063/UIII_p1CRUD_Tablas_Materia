from django.urls import path
from materia_app import views

urlpatterns = [
    path("", views.inicio_vistas, name="inicio_vistas"),
    path("registrarMateria/",views.registrarMateria, name="registrarMateria")
]
