"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from State import views as state_views
from City import views as city_views
from Person import views as person_views
from BloodType import views as bloodtype_views
from BloodCenter import views as bloodcenter_views
from BloodDonation import views as blooddonation_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('states/', state_views.list_states),
    path('states/<int:id>', state_views.state_details),
    path('cities/', city_views.list_cities),
    path('cities/<int:id>', city_views.city_details),
    path('person/', person_views.list_person),
    path('person/<int:id>', person_views.person_details),
    path('bloodtypes/', bloodtype_views.list_bloodtypes),
    path('bloodtypes/<int:id>', bloodtype_views.bloodtype_details),
    path('bloodcenters/<int:id>', bloodcenter_views.bloodcenter_details),
    path('bloodcenters/', bloodcenter_views.list_bloodcenters),
    path('blooddonations/', blooddonation_views.list_blooddonations),
    path('blooddonations/<int:id>', blooddonation_views.blooddonation_details),
]
