from rest_framework import serializers
from .models import DemandForm

class DRFSerial(serializers.ModelSerializer):
    class Meta:
        model = DemandForm
        fields='__all__'


