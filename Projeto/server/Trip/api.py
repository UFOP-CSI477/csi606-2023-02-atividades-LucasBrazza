from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from rest_framework import permissions, serializers, viewsets, status
from rest_framework.response import Response 
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from Vehicles.models import VehicleModel
from .models import TripModel, PassengerTripModel
from .serializers import PassengerTripSerializer, TripSerializer
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
    
class FinishedTripView(DestroyAPIView):
    queryset = TripModel.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsDriverOrSysManager]
    
    

class PassengerTripListView(ListAPIView):
    serializer_class = PassengerTripSerializer
    
    def get_queryset(self):        
        return PassengerTripModel.objects.get(passenger=self.request.user)
    

class DriverTripListView(ListAPIView):
    serializer_class = TripSerializer
    
    def get_queryset(self):
        return TripModel.objects.get(driver=self.request.user)


class BookTripView(CreateAPIView):
    serializer_class = PassengerTripSerializer
    permission_classes = [IsPassengerOrDriver]
    
    def create(self, request, *args, **kwargs):
        # Obtém os dados da solicitação
        trip_id = request.data.get('trip')
        passenger = request.user
        
        # Verifica se a viagem existe
        try:
            trip = TripModel.objects.get(pk=trip_id)
        except TripModel.DoesNotExist:
            return Response({"error": "Viagem não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        
        # Verifica se há vagas disponíveis
        if trip.vacancies <= 0:
            return Response({"error": "Não há vagas disponíveis para esta viagem"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Verifica se o passageiro já está na viagem
        if trip.passengers.filter(passenger).exists():
            return Response({"error": "Você já está nesta viagem"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Cria a relação entre a viagem e o passageiro
        PassengerTripModel.objects.create(trip=trip, passenger_id=passenger)
        
        # Atualiza a quantidade de vagas disponíveis
        trip.vacancies -= 1
        trip.save()
        
        return Response({"success": "Viagem reservada com sucesso"}, status=status.HTTP_201_CREATED)
   