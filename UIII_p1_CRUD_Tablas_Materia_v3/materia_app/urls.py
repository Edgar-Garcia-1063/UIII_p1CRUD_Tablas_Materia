from django.urls import path
from materia_app import views

urlpatterns = [
    path("", views.inicio_vistas, name="inicio_vistas"),
    path("registrarMateria/", views.registrarMateria, name="registrarMateria"),
    path("seleccionarMateria/<codigo>",views.seleccionarMateria,name="seleccionarMateria"),
    path("editarMateria/",views.editarMateria,name="editarMateria"),
    path("BorrarMateria/<codigo>",views.BorrarMateria, name="BorrarMateria")
]
