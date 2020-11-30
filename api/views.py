from django.shortcuts import render
from reservas.models import Habitaciones
from rest_framework import viewsets
from .serializer import HabitacionesSerializers
from rest_framework.decorators import api_view
# from django.http.response import JsonResponse
# from rest_framework.parsers import JSONParser 
# from rest_framework import status


class HabitacionesViewset(viewsets.ModelViewSet):
  queryset = Habitaciones.objects.all()
  serializer_class = HabitacionesSerializers


  
# @api_view(['GET', 'POST', 'DELETE'])
# def habitaciones_list(request):
#     if request.method == 'GET':
#         hab = Habitaciones.objects.all()
        
#         # title = request.query_params.get('title', None)
#         # if title is not None:
#         #     tutorials = tutorials.filter(title__icontains=title)
        
#         serializer_class = HabitacionesSerializers(hab, many=True)
#         return JsonResponse(serializer_class.data, safe=False)
#         # 'safe=False' for objects serialization
 
#     elif request.method == 'POST':
#         habitaciones_data = JSONParser().parse(request)
#         habitaciones_serializer = HabitacionesSerializers(data=habitaciones_data)
#         if habitaciones_serializer.is_valid():
#             habitaciones_serializer.save()
#             return JsonResponse(habitaciones_serializer.data, status=status.HTTP_201_CREATED) 
#         return JsonResponse(habitaciones_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         count = Habitaciones.objects.all().delete()
#         return JsonResponse({'message': '{} Habitaciones fue eliminado con exito!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
# @api_view(['GET', 'PUT', 'DELETE'])
# def habitaciones_detail(request, pk):
#     try: 
#         hab = Habitaciones.objects.get(pk=pk) 
#     except hab.DoesNotExist: 
#         return JsonResponse({'message': 'La habitacion no existe'}, status=status.HTTP_404_NOT_FOUND) 
 
#     if request.method == 'GET': 
#         habitaciones_serializer = habitaciones_serializer(hab) 
#         return JsonResponse(habitaciones_serializer.data) 
 
#     elif request.method == 'PUT': 
#         habitaciones_data = JSONParser().parse(request) 
#         habitaciones_serializer = HabitacionesSerializers(hab, data=habitaciones_data) 
#         if habitaciones_serializer.is_valid(): 
#             habitaciones_serializer.save() 
#             return JsonResponse(habitaciones_serializer.data) 
#         return JsonResponse(habitaciones_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
#     elif request.method == 'DELETE': 
#         hab.delete() 
#         return JsonResponse({'message': 'Habitacion fue eliminado con exito!'}, status=status.HTTP_204_NO_CONTENT)
    
        
# @api_view(['GET'])
# def habitaciones_list_p(request):
#     hab = Tutorial.objects.filter(published=True)
        
#     if request.method == 'GET': 
#         habitaciones_serializer = HabitacionesSerializers(hab, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)