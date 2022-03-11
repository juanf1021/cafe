from django import forms

class FormularioContacto(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group','required': True, 'placeholder':'Nombre', 'autocomplete': 'off'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input-group','required': True, 'placeholder':'Email', 'autocomplete': 'off'}))
    contenido=forms.CharField(widget=forms.Textarea(attrs={'class': 'text-area','required': True, 'placeholder':'Mensaje', 'autocomplete': 'off'}))

