

from django.urls import path

from usuario import views

urlpatterns = [
	path("login/", views.login, name="login"),
	path("listar/", views.listar, name="listar"),
	path("listar/<int:identificador>", views.perfil, name="detalle"),
	path("crear/", views.nuevo),
	path("producto/crear/", views.alta),
	path("eliminar/<int:identificador>", views.eliminar, name="eliminar"),
	path("modificar/<int:identificador>", views.modificar, name="modificar"),
	path("pruebas/", views.prueba, name="home"),
	path("cards/", views.cards, name="cards")
]