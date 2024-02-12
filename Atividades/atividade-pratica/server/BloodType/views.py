from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import BloodType
from .serializers import BloodTypeSerializer

@api_view(['GET', 'POST'])
def list_bloodtypes(request):
    
    if request.method == 'GET':
        bloodtypes = BloodType.objects.all()
        serializer = BloodTypeSerializer(bloodtypes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BloodTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def bloodtype_details(request, id):
    
    try:
        bloodtype = BloodType.objects.get(pk=id)
    except BloodType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BloodTypeSerializer(bloodtype)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = BloodTypeSerializer(bloodtype, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        bloodtype.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)