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
from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from users.views import login, registro, logout, ver_perfil
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

    
    # login y registro
    # path('', views.welcome),
    # path('register', views.register),
    # path('login', views.login),
    # path('logout', views.logout),
    
    # cambie los Path de login y registro por el include de abajo 
    path('', views.home), #añadi las url home de inicio
    

    path('admin/', admin.site.urls),
    path('home/', views.home), #añadi las url home
    path('habitaciones/', views.habitaciones), #añadi las url habitaciones
    path('galeria/', views.galeria), #añadi las url galeria
    path('sobre_nosotros/', views.sobre_nosotros), #añadi las url sobre_nosotros
    path('Pucon/', views.Departamento_pucon), #añadi las url habitacion_vip
    path('La_Serena/', views.Departamento_laserena), #añadi las url habitacion_vip
    path('Viña_del_Mar/', views.Departamento_viñadelmar), #añadi las url habitacion_vip
    path('Puerto_Varas/', views.Departamento_puertovaras), #añadi las url habitacion_vip
    path('Iquique/', views.Departamento_iquique), #añadi las url habitacion_vip
    path('Buscar_Fecha/', views.Buscar_fecha), #añadi las url habitacion_vip
    path('login/', login), #añadi las url login
    path('usuario/', include('users.urls')), #añadi las urls que tendrá el sistema de reservas en un path solo 'reservas/'
    path('reservar/', include('reservas.urls')), #añadi las urls que tendrá el sistema de reservas en un path solo 'users/'
    path('contacto/', include('contacto.urls')), #añadi las urls que tendrá el sistema de reservas en un path solo 'contacto/'
    path('registro/', registro),
    path('perfil/', ver_perfil),
    path('logout/', logout),
    path('comentarios/', include('comentarios.urls')), #añadí la urls para el sistema de comentarios
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)