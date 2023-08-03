from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse
from inicio.forms import AutoForm, BuscarAuto, ModificarAutoForm
from inicio.models import Auto
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def inicio (request):
    return render(request,'inicio/inicio.html')

def acerca_de_mi (request):
    return render(request,'inicio/acerca_de_mi.html')

    
class CrearAuto(LoginRequiredMixin,CreateView):
   model = Auto
   template_name = 'inicio/CBV/crear_autos_CBV.html'
   fields = ['marca', 'modelo', 'anio','descripcion']
   success_url = reverse_lazy('inicio:buscar_autos')
   
class BuscarAuto (ListView):
    model = Auto
    template_name = "inicio/CBV/buscar_autos_CBV.html"
    context_object_name = 'autos'
    
    

class ModificarAuto(LoginRequiredMixin, UpdateView):
    model = Auto
    template_name = "inicio/CBV/modificar_autos_CBV.html"
    fields = ['marca', 'modelo', 'anio','descripcion']
    success_url = reverse_lazy('inicio:buscar_autos')

class EliminarAuto(LoginRequiredMixin,DeleteView):
    model = Auto
    template_name = "inicio/CBV/eliminar_autos_CBV.html"
    success_url = reverse_lazy('inicio:buscar_autos')

class MostrarAuto(LoginRequiredMixin,DetailView):
    model = Auto
    template_name = "inicio/CBV/mostrar_autos_CBV.html"
  

