from django.views.generic import ListView, FormView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Driver
from .forms import DriverForm



class DriverLoginView(LoginView):
    template_name = 'driver_login.html'
    success_url = reverse_lazy('driver_dashboard')

    def form_valid(self, form):
        remember_me = self.request.POST.get('remember_me')
        if remember_me:
            self.request.session.set_expiry(60 * 60 * 24 * 30)  # Expires in 30 days
        else:
            self.request.session.set_expiry(0)  # Sessão expira quando o navegador é fechado
        return super().form_valid(form)
    


class DriversList(ListView):
    model = Driver
    template_name = 'Driver/drivers_list.html'
    context_object_name = 'drivers'
    paginate_by = 6
    
    # @api_view(['GET'])
    def get_queryset(self):
        return super().get_queryset().order_by('type')
    
# fix csrf ond DriverFormView
class DriverFormView(FormView):
    template_name = 'Driver/driver_create.html'
    form_class = DriverForm
    success_url = reverse_lazy('drivers-list')
    
    # @api_view(['POST'])
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("form_invalid")
        return super().form_invalid(form)

class DriverUpdateView(UpdateView):
    model = Driver
    template_name = 'Driver/driver_details.html'
    form_class = DriverForm
    success_url = reverse_lazy('drivers-list')
    
    # @api_view(['POST'])
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("form_invalid: ", form)
        return super().form_invalid(form)
    

class DriverDeleteView(DeleteView):
    model = Driver
    success_url = reverse_lazy('drivers-list')

    def form_valid(self, form):
        driver_id = self.kwargs['pk']
        driver = Driver.objects.get(pk=driver_id) 
        driver.delete() 
        return super().form_valid(form)
    