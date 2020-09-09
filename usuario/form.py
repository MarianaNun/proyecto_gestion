
from django.forms import ModelForm
from usuario.models import Producto, Visitante

from django import forms


class FormProducto(ModelForm):

	class Meta:
		model = Producto
		fields = ['nombre', 'precio']
	
	nombre = forms.CharField(label='Name:',max_length=15,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control col-sm-5 my-1',
                                        'placeholder':'Name'
                                    }))

class FormUsuario(ModelForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)
    telefono = forms.CharField(max_length=30)
    domicilio = forms.CharField(max_length=100)
    password1 = forms.CharField(max_length=30)
    password2 = forms.CharField(max_length=30)

    class Meta:
    	model = Visitante
    	fields = (
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'telefono',
            'domicilio',
        )