from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import State
from .serializers import StateSerializer


@api_view(['GET', 'POST'])
def list_states(request):
    
    if request.method == 'GET':
        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        return Response(serializer.data)
        # return render(request, 'State/list_states.html')
        
    
    if request.method == 'POST':
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


@api_view(['GET', 'PUT', 'DELETE'])
def state_details(request, id):
    try:
        state = State.objects.get(pk=id)
    except State.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StateSerializer(state)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = StateSerializer(state, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        state.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)