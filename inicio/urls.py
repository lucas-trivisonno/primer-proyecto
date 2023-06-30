from django.urls import path
from inicio import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('agregar-datos/', views.agregar_datos, name='agregar-datos'),
    path('buscar/', views.buscar, name='buscar'),
]
