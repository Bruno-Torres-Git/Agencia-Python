from django.contrib import admin
from agencia.models import *
# Register your models here.
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre','telefono')
    search_fields = ('nombre','telefono')
    
class ViajeAdmin(admin.ModelAdmin):
    list_display = ('destino','empresa')
    search_fields = ('destino','empresa')


admin.site.register(Empresa,EmpresaAdmin)
admin.site.register(Viaje,ViajeAdmin)
