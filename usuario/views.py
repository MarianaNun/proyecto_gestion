
from django.shortcuts import render, redirect

from django.http import HttpResponse

from usuario.models import Visitante

from usuario.form import FormProducto, FormUsuario

# Create your views here.
def login(request):

	return render(request, "base.html")



def listar(request):
	if request.user.is_authenticated:
		lista = Visitante.objects.all().order_by('email')
		context = {"usuarios": lista}
		return render(request, 'listar.html', context)
	return redirect('crear/')


def perfil(request, identificador):
	usuario = Visitante.objects.get(id=identificador)
	context = {"dato": usuario}
	return render(request, 'detalle.html', context)


def nuevo(request):
	if request.POST:
		post = request.POST
#		nuevo_usuario = Usuario(post['id'], post['nombre'], post['telefono'], post['email'], post['contrasena'], post['domicilio'])
		datos = FormUsuario(request.POST)
		if datos.is_valid:
			datos.save()
	return render(request, 'nuevo.html')

def alta(request):
	if request.method == 'POST':
		datos = FormProducto(request.POST)
	#	producto = Producto(2, datos['nombre'], datos['descripcion'], datos['precio'])
		datos.save()
	else:
		datos = FormProducto()
	context = {"cualquiercosa": datos}

	return render(request, 'producto_nuevo.html', context)

def eliminar(request, identificador):
	usuario = Visitante.objects.get(id=identificador)
	usuario.delete()

	return redirect('listar')


def modificar(request, identificador):
	if request.method == "POST":
		post = request.POST
		usuario = FormUsuario(request.POST)
		usuario.save()
		return redirect('detalle', identificador)

	else:
		usuario = Visitante.objects.get(id=identificador)
	context = {"datos": usuario}
	
	return render(request, "modificar.html", context)


def prueba(request):
	return render(request, "prueba.html")

def cards(request):
	return render(request, "cards.html")