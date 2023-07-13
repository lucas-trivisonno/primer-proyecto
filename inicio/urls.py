from django.urls import path
from inicio import views

app_name ='inicio'

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('crear_autos/', views.crear_auto, name='crear_autos'),
    path('buscar/', views.buscar, name='buscar'),
]
