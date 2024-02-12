from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import BloodCenter
from .serializers import BloodCenterSerializer

class BloodCentersList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Location/blood_centers_list.html'

    def get(self, request):
        blood_centers = BloodCenter.objects.all()
        serializer = BloodCenterSerializer(blood_centers, many=True)
        return Response({"blood_centers":serializer.data})
    
    def post(self, request):
        serializer = BloodCenterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class BloodCenterDetails(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Location/blood_center_details.html'

    def get(self, request, id):
        blood_center = get_object_or_404(BloodCenter, pk=id)
        serializer = BloodCenterSerializer(blood_center)
        return Response({'serializer': serializer, 'blood_center': blood_center})
    
    def put(self, request, id):
        blood_center = get_object_or_404(BloodCenter, pk=id)
        serializer = BloodCenterSerializer(blood_center, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'serializer': serializer, 'blood_center': blood_center}) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        blood_center = get_object_or_404(BloodCenter, pk=id)
        blood_center.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    