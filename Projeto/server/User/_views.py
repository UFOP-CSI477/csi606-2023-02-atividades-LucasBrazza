from django.contrib.auth import logout
from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import login

from .models import UserModel

from User.permissions import IsOwnerOrSysManager

from .forms import LoginForm, UserDriverForm, UserPassengerForm

class LoginView(generic.FormView):
    model = UserModel
    form_class = LoginForm
    template_name = 'Auth/login.html'
    success_url = '/'
    
    def get_success_url(self):
        # Redirect to the homepage after successful login
        print(self.request.user)
        return render(self.request, 'index.html', {'user_id': self.request.user.cpf})

    def post(self, request, *args, **kwargs):
        user = UserModel.objects.filter(cpf=request.POST['username']).first()
        login(request, user)

        # Pass the user object to the context
        context = {'user': user}
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK, template_name='index.html', context=context)
      
class LogoutView(generic.View):
    success_url = '/'
    def get(self, request):
        logout(request)
        return redirect('login')  # Redirecione para a página de login após o logout


class CreateDriverUserView(generic.CreateView):
    form_class = UserDriverForm
    template_name = 'User/register_driver.html'
    success_url = reverse_lazy('login')
    

class CreatePassengerUserView(generic.CreateView):
    form_class = UserPassengerForm
    template_name = 'User/register_passenger.html'
    success_url = reverse_lazy('login')


class UpdateDriverUserView(generic.UpdateView):
    model = UserModel
    form_class = UserDriverForm
    template_name = 'User/update_driver.html'
    success_url = reverse_lazy('homepage')
           
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        print(self.request.user)
        if not IsOwnerOrSysManager().has_permission(self.request, self):
            return HttpResponseForbidden("Você não tem permissão para criar este objeto.")
        self.object = form.save()
    

class UpdatePassengerUserView(generic.UpdateView):
    form_class = UserPassengerForm
    template_name = 'User/update_passenger.html'
    success_url = '/login'
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        print(self.request.user)
        if not IsOwnerOrSysManager().has_permission(self.request, self):
            return HttpResponseForbidden("Você não tem permissão para criar este objeto.")
        self.object = form.save()
        return super().form_valid(form)
    
class DeleteUserView(generic.DeleteView):
    model = UserModel
    success_url = reverse_lazy('homepage')
    
    def delete(self, request, *args, **kwargs):
        if not IsOwnerOrSysManager().has_permission(request, self):
            return HttpResponseForbidden("Você não tem permissão para deletar este objeto.")
        return super().delete(request, *args, **kwargs)

class HomeView(generic.TemplateView):
    template_name = 'index.html'