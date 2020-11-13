from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.paciente, name= "paciente"),
    path('busqueda/',views.busqueda, name = "busqueda"),
    path('medico/',views.medico, name="medico")
]