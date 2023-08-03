from django import forms
from ckeditor.fields import RichTextFormField
class AutoFormPadre(forms.Form):
    marca = forms.CharField(max_length=100)
    modelo = forms.CharField(max_length=100)
    anio = forms.IntegerField()
    descripcion = RichTextFormField()
    
class AutoForm(AutoFormPadre):
    ...

class ModificarAutoForm(AutoFormPadre):
    ...    

class BuscarAuto(forms.Form):
    marca= forms.CharField(max_length=100, required= False)