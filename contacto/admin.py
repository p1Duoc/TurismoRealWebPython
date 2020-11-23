from django.contrib import admin
from .models import contacto

# Register your models here.

#admin.site.register(contacto)
@admin.register(contacto)
class contacto(admin.ModelAdmin):
    list_display = ('first_name','last_name','phone','email')