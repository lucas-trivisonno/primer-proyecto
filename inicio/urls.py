from django.urls import path
from inicio import views

app_name ='inicio'

urlpatterns = [
    path('',views.inicio, name='inicio'),
    #  path('crear_autos/', views.crear_auto, name='crear_autos'),
    # path('buscar/', views.buscar, name='buscar'),
    # path('eliminar/<int:auto_id>/', views.eliminar, name='eliminar'),
    # path('modificar_auto/<int:auto_id>/', views.modificar_auto, name='modificar_auto'),
     
    
    path('crear_autos/', views.CrearAuto.as_view(), name='crear_autos'),
    path('buscar/', views.BuscarAuto.as_view(), name='buscar_autos'),
    path('eliminar/<int:pk>/', views.EliminarAuto.as_view(), name='eliminar_autos'),
    path('modificar_auto/<int:pk>/', views.ModificarAuto.as_view(), name='modificar_autos'),
    path('mostrar_auto/<int:pk>/', views.MostrarAuto.as_view(), name='mostrar_autos'),
]
