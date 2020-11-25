"""Hotel_bit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views
from users.views import login, registro, logout, ver_perfil
urlpatterns = [

    
    # login y registro
    # path('', views.welcome),
    # path('register', views.register),
    # path('login', views.login),
    # path('logout', views.logout),
    
    path('', views.home),
    

    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('habitaciones/', views.habitaciones),
    path('galeria/', views.galeria),
    path('sobre_nosotros/', views.sobre_nosotros),
    path('Pucon/', views.Departamento_pucon),
    path('La_Serena/', views.Departamento_laserena),
    path('Viña_del_Mar/', views.Departamento_viñadelmar),
    path('Puerto_Varas/', views.Departamento_puertovaras),
    path('Iquique/', views.Departamento_iquique),
    path('login/', login),
    path('usuario/', include('users.urls')),
    path('reservar/', include('reservas.urls')),
    path('contacto/', include('contacto.urls')),
    path('registro/', registro),
    path('perfil/', ver_perfil),
    path('logout/', logout),
    path('comentarios/', include('comentarios.urls')),
    
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
