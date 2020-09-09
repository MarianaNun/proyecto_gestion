from django.contrib import admin

# Register your models here.

from usuario.models import Visitante, Producto

def modificar_email(modeladmin, request, queryset):
	queryset.update(email='email@test.com')
	modificar_email.short_description = "Modificame el email"



class UsuarioAdmin(admin.ModelAdmin):
	list_display = ('user',)
	actions = [modificar_email]


admin.site.register(Visitante)
admin.site.register(Producto)