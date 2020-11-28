from reservas.models import Habitaciones
from rest_framework import serializers

class HabitacionesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Habitaciones
        fields = '__all__'
