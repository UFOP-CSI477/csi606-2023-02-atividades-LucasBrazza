from django.urls import path
from . import views

urlpatterns = [
    path('client/signup/', views.CreateClientUserView.as_view(), name='singup-client'),
    path('driver/singup/', views.CreateDriverUserView.as_view(), name='singup-driver'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # outras URLs do seu aplicativo
]