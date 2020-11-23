from django.contrib import admin
from django.contrib.auth.models import User

from.models import Profile

admin.site.register(Profile)
admin.site.site_header = "Turismo Real - Sistema de Arriendos"
admin.site.site_title = "Portal Administración - Turismo Real"
admin.site.index_title = "Bienvenidos al portal de administración"


