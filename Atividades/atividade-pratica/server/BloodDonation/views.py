from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import BloodDonation
from .serializers import BloodDonationSerializer

@api_view(['GET', 'POST'])
def list_blooddonations(request):
    
    if request.method == 'GET':
        blooddonations = BloodDonation.objects.all()
        serializer = BloodDonationSerializer(blooddonations, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BloodDonationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def blooddonation_details(request, id):
    
    try:
        blooddonation = BloodDonation.objects.get(pk=id)
    except BloodDonation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BloodDonationSerializer(blooddonation)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = BloodDonationSerializer(blooddonation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        blooddonation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)