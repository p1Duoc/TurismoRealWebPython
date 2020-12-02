from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, Usuario_Extension
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.site_header = "Turismo Real - Sistema de Arriendos"
admin.site.site_title = "Portal Administración - Turismo Real"
admin.site.index_title = "Bienvenidos al portal de administración"

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Usuario_Extension
    can_delete = False
    verbose_name_plural = 'Detalles Usuarios'
S    
# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)