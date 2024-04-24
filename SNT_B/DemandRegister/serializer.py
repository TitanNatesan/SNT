from rest_framework import serializers
from .models import DemandForm,Complaint

class DRFSerial(serializers.ModelSerializer):
    class Meta:
        model = DemandForm
        fields='__all__'

class CompSerial(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields ='__all__'