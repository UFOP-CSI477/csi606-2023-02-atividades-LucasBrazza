from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import BloodDonation
from .serializers import BloodDonationSerializer

class BloodDonationsList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Donation/blood_donations_list.html'

    def get(self, request):
        blood_donations = BloodDonation.objects.all()
        serializer = BloodDonationSerializer(blood_donations, many=True)
        return Response({"blood_donations":serializer.data})
    
    def post(self, request):
        serializer = BloodDonationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class BloodDonationDetails(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Donation/blood_donation_details.html'

    def get(self, request, id):
        blood_donation = get_object_or_404(BloodDonation, pk=id)
        serializer = BloodDonationSerializer(blood_donation)
        return Response({'serializer': serializer, 'blood_donation': blood_donation})
    
    def put(self, request, id):
        blood_donation = get_object_or_404(BloodDonation, pk=id)
        serializer = BloodDonationSerializer(blood_donation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'serializer': serializer, 'blood_donation': blood_donation}) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        blood_donation = get_object_or_404(BloodDonation, pk=id)
        blood_donation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    