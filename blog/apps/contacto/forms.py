from django import forms
from .models import Contacto

# Register your models here.
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre_apellido','email','asunto','fecha']
    