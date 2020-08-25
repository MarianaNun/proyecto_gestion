from django.shortcuts import render

import datetime

class Persona():
	def __init__(self,nombre, edad):
		self.nombre = nombre
		self.edad = edad

def saludo(request, horas):
	now =datetime.datetime.now()
	hora = now + datetime.timedelta(hours=horas)
	persona = Persona("Juan", 30)
	context = {'hora':now, 'adelantado':hora, 'valor': horas, 'datos': persona, 'lista':["elemento1", "elemento2", "elemento3"], "dato":{}}
	return render(request, "saludo.html", context )