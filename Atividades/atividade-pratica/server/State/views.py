from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import State
from .serializers import StateSerializer

class StatesList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Location/states_list.html'

    def get(self, request):
        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        return Response({"states":serializer.data})
    
    def post(self, request):
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class StateDetails(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Location/state_details.html'

    def get(self, request, id):
        state = get_object_or_404(State, pk=id)
        serializer = StateSerializer(state)
        return Response({'serializer': serializer, 'state': state})
    
    def put(self, request, id):
        state = get_object_or_404(State, pk=id)
        serializer = StateSerializer(state, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'serializer': serializer, 'state': state}) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        state = get_object_or_404(State, pk=id)
        state.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    