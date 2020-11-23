from django.contrib import admin
from .models import Habitacion, Reservas_habitacion, Reserva, Habitaciones, \
    Tipo_pension, Precio_pension, Tipo_alojamiento, CantidadReservas , ProductosDeptos, \
    DetalleDepto, Comuna

# Register your models here.

admin.site.register(Reservas_habitacion)
admin.site.register(Reserva)
#admin.site.register(Habitaciones)
admin.site.register(Tipo_pension)
admin.site.register(Precio_pension)
admin.site.register(Tipo_alojamiento)
admin.site.register(CantidadReservas)
#admin.site.register(ProductosDeptos)
#admin.site.register(DetalleDepto)
#admin.site.register(Comuna)



@admin.register(Habitaciones)
class Habitaciones(admin.ModelAdmin):
    list_display = ('Dirección_Departamento', 'Número', 'idcomuna', 'Precio')

@admin.register(Comuna)
class Comuna(admin.ModelAdmin):
    list_display = ('Comuna', 'Ciudad')

@admin.register(ProductosDeptos)
class ProductosDeptos(admin.ModelAdmin):
    list_display = ('Nombre', 'Descripción','Valor')

@admin.register(DetalleDepto)
class DetalleDepto(admin.ModelAdmin):
    list_display = ('iddepto','idproductos','qprod')
