from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import BloodCenter
from .serializers import BloodCenterSerializer

@api_view(['GET', 'POST'])
def list_bloodcenters(request):
    
    if request.method == 'GET':
        bloodcenters = BloodCenter.objects.all()
        serializer = BloodCenterSerializer(bloodcenters, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BloodCenterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def bloodcenter_details(request, id):
    
    try:
        bloodcenter = BloodCenter.objects.get(pk=id)
    except BloodCenter.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BloodCenterSerializer(bloodcenter)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = BloodCenterSerializer(bloodcenter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        bloodcenter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)