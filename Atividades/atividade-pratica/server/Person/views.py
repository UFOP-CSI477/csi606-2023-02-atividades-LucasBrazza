from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Person
from .serializers import PersonSerializer

class PersonsList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Location/persons_list.html'

    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response({"persons":serializer.data})
    
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class PersonDetails(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Location/person_details.html'

    def get(self, request, id):
        person = get_object_or_404(Person, pk=id)
        serializer = PersonSerializer(person)
        return Response({'serializer': serializer, 'person': person})
    
    def put(self, request, id):
        person = get_object_or_404(Person, pk=id)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'serializer': serializer, 'person': person}) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        person = get_object_or_404(Person, pk=id)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    