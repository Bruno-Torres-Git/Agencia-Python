from django.forms import ModelForm, Textarea
from django import forms

class ContactoForm(forms.Form):
    correo = forms.EmailField()
    mensaje = forms.CharField(widget=Textarea)