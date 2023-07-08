from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .forms import AutoForm
# Create your views here.
def inicio (request):
    return render(request,'inicio/inicio.html')


def crear_auto(request):
    form = AutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AutoForm()
    context = {
        'form': form
    }
    return render(request, 'inicio/crear_autos.html', context)

def buscar(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        autos = autos.objects.filter(marca__icontains=query)
        context = {
            'query': query,
            'autos': autos
        }
        return render(request, 'inicio/buscar.html', context)
    return render(request, 'inicio/buscar.html')
