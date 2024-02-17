from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from rest_framework import permissions, serializers, viewsets, status
from rest_framework.response import Response 
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from Vehicles.models import VehicleModel
from .models import TripModel, PassengerTripModel
from .serializers import PassengerTripModelSerializer, TripSerializer
from User.permissions import IsDriverOrSysManager, IsPassengerOrDriver, IsNotAuthenticated

class TripCreateView(CreateAPIView):
    queryset = TripModel.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsDriverOrSysManager]

    def perform_create(self, serializer):
        # Set the driver to the current user
        serializer.save(driver=self.request.user)


class ListTripView(ListAPIView):
    queryset = TripModel.objects.all()
    serializer_class = TripSerializer
    

class SearchTripView(ListAPIView):
    queryset = TripModel.objects.all()
    serializer_class = TripSerializer
    
    def get_queryset(self):
        queryset = TripModel.objects.all()
        origin = self.request.query_params.get('origin', None)
        destination = self.request.query_params.get('destination', None)
        day = self.request.query_params.get('day', None)
        
        if origin:
            queryset = queryset.filter(origin__icontains=origin)
        if destination:
            queryset = queryset.filter(destination__icontains=destination)
        if day:
            queryset = queryset.filter(day=day)
        
        return queryset
    
class CompleteTripView(DestroyAPIView):
    queryset = TripModel.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsDriverOrSysManager]
    
    

class UserTripListView(ListAPIView):
    serializer_class = TripSerializer
    
    def get_queryset(self):
        queryset = TripModel.objects.all()
        user_id = self.request.user.id
        user_type = self.request.user.type
        
        if user_type == 'driver':
            queryset = queryset.filter(driver_id=user_id)
        elif user_type == 'passenger':
            queryset = queryset.filter(passengers__id=user_id)
        
        return queryset

class BookTripView(CreateAPIView):
    serializer_class = PassengerTripModelSerializer
    permission_classes = [IsPassengerOrDriver]
    
    def create(self, request, *args, **kwargs):
        # Obtém os dados da solicitação
        trip_id = request.data.get('trip')
        passenger_id = request.user.id
        
        # Verifica se a viagem existe
        try:
            trip = TripModel.objects.get(pk=trip_id)
        except TripModel.DoesNotExist:
            return Response({"error": "Viagem não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        
        # Verifica se há vagas disponíveis
        if trip.vacancies <= 0:
            return Response({"error": "Não há vagas disponíveis para esta viagem"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Verifica se o passageiro já está na viagem
        if trip.passengers.filter(id=passenger_id).exists():
            return Response({"error": "Você já está nesta viagem"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Cria a relação entre a viagem e o passageiro
        PassengerTripModel.objects.create(trip=trip, passenger_id=passenger_id)
        
        # Atualiza a quantidade de vagas disponíveis
        trip.vacancies -= 1
        trip.save()
        
        return Response({"success": "Viagem reservada com sucesso"}, status=status.HTTP_201_CREATED)
   