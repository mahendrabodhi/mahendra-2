# destinations/serializers.py
from rest_framework import serializers
from .models import Destination

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'  # Include all fields from the Destination model
