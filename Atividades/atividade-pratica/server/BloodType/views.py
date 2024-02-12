from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import BloodType
from .serializers import BloodTypeSerializer

class BloodTypesList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Location/blood_types_list.html'

    def get(self, request):
        blood_types = BloodType.objects.all()
        serializer = BloodTypeSerializer(blood_types, many=True)
        return Response({"blood_types":serializer.data})
    
    def post(self, request):
        serializer = BloodTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class BloodTypeDetails(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Location/blood_type_details.html'

    def get(self, request, id):
        blood_type = get_object_or_404(BloodType, pk=id)
        serializer = BloodTypeSerializer(blood_type)
        return Response({'serializer': serializer, 'blood_type': blood_type})
    
    def put(self, request, id):
        blood_type = get_object_or_404(BloodType, pk=id)
        serializer = BloodTypeSerializer(blood_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'serializer': serializer, 'blood_type': blood_type}) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        blood_type = get_object_or_404(BloodType, pk=id)
        blood_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    