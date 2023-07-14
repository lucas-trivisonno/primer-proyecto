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
# Create your views here.
def inicio (request):
    return render(request,'inicio/inicio.html')


# def crear_auto(request):
    
#  if request.method == "POST":
#      formulario = AutoForm(request.POST)
#      if formulario.is_valid():
#         info = formulario.cleaned_data
#         auto = Auto (marca=info['marca'], modelo=info['modelo'], anio=info['anio'])
#         auto.save()
#         return redirect('inicio:buscar' )
#      else :
#         return render(request, 'inicio/crear_autos.html', {'formulario' : formulario})
    
#  formulario = AutoForm()
#  return render(request, 'inicio/crear_autos.html', {'formulario' : formulario})

# def buscar(request):
#     formulario = BuscarAuto(request.GET)
#     if formulario.is_valid():
#        marca_a_buscar = formulario.cleaned_data['marca']
#        listado_de_autos = Auto.objects.filter(marca__icontains=marca_a_buscar)
       
#     return render(request, 'inicio/buscar.html', {'formulario' : formulario, 'autos':listado_de_autos})
 

# def eliminar(request, auto_id):
   
#    auto = Auto.objects.get(id=auto_id)
#    auto.delete()
   
#    return redirect('inicio:buscar')

# def modificar_auto(request, auto_id):
#     auto_a_modificar = Auto.objects.get(id=auto_id)
   
#     if request.method == 'POST':
#       formulario = ModificarAutoForm(request.POST)
      
#       if formulario.is_valid():
#          info = formulario.cleaned_data
#          auto_a_modificar.marca = info['marca']
#          auto_a_modificar.modelo = info['modelo']
#          auto_a_modificar.anio = info['anio']
#          auto_a_modificar.save()
#          return redirect('inicio:buscar')
         
#       else:
#            return(request, 'inicio/modificar_auto.html', {'formulario':formulario}) 
    
#     formulario = ModificarAutoForm(initial={'marca':auto_a_modificar.marca, 'modelo':auto_a_modificar.modelo, 'anio':auto_a_modificar.anio})
#     return render(request, 'inicio/modificar_auto.html', {'formulario':formulario})
    
class CrearAuto(CreateView):
   model = Auto
   template_name = 'inicio/CBV/crear_autos_CBV.html'
   fields = ['marca', 'modelo', 'anio','descripcion']
   success_url = reverse_lazy('inicio:buscar_autos')
   
class BuscarAuto (ListView):
    model = Auto
    template_name = "inicio/CBV/buscar_autos_CBV.html"
    context_object_name = 'autos'

class ModificarAuto(UpdateView):
    model = Auto
    template_name = "inicio/CBV/modificar_autos_CBV.html"
    fields = ['marca', 'modelo', 'anio','descripcion']
    success_url = reverse_lazy('inicio:buscar_autos')

class EliminarAuto(DeleteView):
    model = Auto
    template_name = "inicio/CBV/eliminar_autos_CBV.html"
    success_url = reverse_lazy('inicio:buscar_autos')

class MostrarAuto(DetailView):
    model = Auto
    template_name = "inicio/CBV/mostrar_autos_CBV.html"
  

