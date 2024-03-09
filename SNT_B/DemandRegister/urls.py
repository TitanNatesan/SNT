from django.urls import path
from . import views


urlpatterns = [
    path("DemandRegister/",views.demandRegister,name="Demand Register"),
    path("getDR/",views.getDR,name='Get Dr')
]

