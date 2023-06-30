from django.shortcuts import render
from .forms import MarcaForm, AutoForm, ConductorForm, BusquedaForm


# Create your views here.
def inicio (request):
    return render(request,'inicio/inicio.html')


def agregar_datos(request):
    marca_form = MarcaForm(request.POST or None)
    auto_form = AutoForm(request.POST or None)
    conductor_form = ConductorForm(request.POST or None)

    if request.method == 'POST':
        if marca_form.is_valid() and auto_form.is_valid() and conductor_form.is_valid():
            marca_form.save()
            auto_form.save()
            conductor_form.save()

    context = {
        'marca_form': marca_form,
        'auto_form': auto_form,
        'conductor_form': conductor_form,
    }

    return render(request, 'inicio/agregar-datos.html', context)

def buscar(request):
    busqueda_form = BusquedaForm(request.POST or None)
    resultados = []

    if request.method == 'POST':
        if busqueda_form.is_valid():
            termino_busqueda = busqueda_form.cleaned_data['termino_busqueda']
            

    context = {
        'busqueda_form': busqueda_form,
        'resultados': resultados,
    }

    return render(request, 'inicio/buscar.html', context)
