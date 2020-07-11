from django.contrib import admin
from .models import Usuario, Paciente, Insumo, InsumoMedico, Reserva, OrdenCompra
#from apps.core.models import Usuario, Paciente
# Register your models here.


class AdminUsuario(admin.ModelAdmin):
    list_display = ('rut','nombre1','apellido_pat', 'apellido_mat')
    search_fields = ['rut', 'nombre1', 'apellido_pat']


class AdminReserva(admin.ModelAdmin):
    list_display = ('nombre','apellido','correo','especialidad','fecha_atencion','hora_atencion','odontologo')
    search_fields = ['nombre','apellido','correo','especialidad']


class AdminInsumo(admin.ModelAdmin):
    list_display = ('codigo','nombre','marca','unid_medida','fecha_vencimiento','cantidad')
    search_fields = ['codigo','nombre','marca']    


admin.site.register(Usuario, AdminUsuario)
admin.site.register(Paciente)
admin.site.register(Insumo, AdminInsumo)
admin.site.register(InsumoMedico)
admin.site.register(Reserva, AdminReserva)
admin.site.register(OrdenCompra)
