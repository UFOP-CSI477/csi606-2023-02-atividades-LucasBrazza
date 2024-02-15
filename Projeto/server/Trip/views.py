from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import TripForm
from .models import Trip

class TripList(ListView):
    model = Trip
    template_name = 'trip_list.html'
    context_object_name = 'trip'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        origin = self.request.GET.get('origin')
        destination = self.request.GET.get('destination')
        date = self.request.GET.get('date')
        
        if origin and destination and date:
            # Faz a pesquisa usando os parâmetros fornecidos
            queryset = queryset.filter(origin=origin, destination=destination, date=date)
        else:
            # Retorna todas as viagens se nenhum parâmetro de pesquisa for fornecido
            queryset = Trip.objects.none()
        
        return queryset


class TripCreateView(CreateView):
    model = Trip
    template_name = 'trip_create.html'
    form_class = TripForm
    success_url = reverse_lazy('trip-list')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("form_invalid")
        return super().form_invalid(form)