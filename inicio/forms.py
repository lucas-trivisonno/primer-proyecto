from django import forms

class AutoForm(forms.Form):
    marca = forms.CharField(max_length=100)
    modelo = forms.CharField(max_length=100)
    anio = forms.IntegerField()

class BuscarAuto(forms.Form):
    marca= forms.CharField(max_length=100, required= False)