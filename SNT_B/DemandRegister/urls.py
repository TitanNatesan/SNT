from django.urls import path
from . import views


urlpatterns = [
    path("DemandRegister/",views.demandRegister,name="Demand Register"),
    path("getDR/",views.getDR,name='Get Dr'),
    path('complaint1/',views.raiseComplaint,name='Raise Complaint'),
    path('getDemand/',views.getRaisedDemand,name='Get Raised Demands'),
]

