from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse
from inicio.forms import AutoForm, BuscarAuto
from inicio.models import Auto
# Create your views here.
def inicio (request):
    return render(request,'inicio/inicio.html')


def crear_auto(request):
    
 if request.method == "POST":
     formulario = AutoForm(request.POST)
     if formulario.is_valid():
        info = formulario.cleaned_data
        auto = Auto (marca=info['marca'], modelo=info['modelo'], anio=info['anio'])
        auto.save()
        return redirect(request, 'inicio/buscar.html', )
     else :
        return render(request, 'inicio/crear_autos.html', {'formulario' : formulario})
    
 formulario = AutoForm()
 return render(request, 'inicio/crear_autos.html', {'formulario' : formulario})

def buscar(request):
    formulario = BuscarAuto(request.GET)
    if formulario.is_valid():
       marca_a_buscar = formulario.cleaned_data['marca']
       listado_de_autos = Auto.objects.filter(marca__icontains=marca_a_buscar)
       
    return render(request, 'inicio/buscar.html', {'formulario' : formulario, 'autos':listado_de_autos})
