from django.shortcuts import render
from reservas.models import Habitaciones
from rest_framework import viewsets
from .serializer import HabitacionesSerializers

class HabitacionesViewset(viewsets.ModelViewSet):
  queryset = Habitaciones.objects.all()
  serializer_class = HabitacionesSerializers