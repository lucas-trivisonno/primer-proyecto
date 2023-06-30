from django import forms
from .models import Marca, Auto, Conductor

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = '__all__'

class ConductorForm(forms.ModelForm):
    class Meta:
        model = Conductor
        fields = '__all__'

class BusquedaForm(forms.Form):
    termino_busqueda = forms.CharField(max_length=100)
