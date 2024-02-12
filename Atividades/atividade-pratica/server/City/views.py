from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import City
from .serializers import CitySerializer

class CitiesList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Location/cities_list.html'

    def get(self, request):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response({"cities":serializer.data})
    
    def post(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class CityDetails(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Location/city_details.html'

    def get(self, request, id):
        city = get_object_or_404(City, pk=id)
        serializer = CitySerializer(city)
        return Response({'serializer': serializer, 'city': city})
    
    def put(self, request, id):
        city = get_object_or_404(City, pk=id)
        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'serializer': serializer, 'city': city}) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        city = get_object_or_404(City, pk=id)
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    