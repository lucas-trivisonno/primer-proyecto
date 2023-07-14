from django import forms

class AutoFormPadre(forms.Form):
    marca = forms.CharField(max_length=100)
    modelo = forms.CharField(max_length=100)
    anio = forms.IntegerField()
    
class AutoForm(AutoFormPadre):
    ...

class ModificarAutoForm(AutoFormPadre):
    ...    

class BuscarAuto(forms.Form):
    marca= forms.CharField(max_length=100, required= False)