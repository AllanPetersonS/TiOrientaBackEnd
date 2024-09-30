# serializers.py
from rest_framework import serializers
from .models import BusLocation, Bus

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ['id', 'bus_number', 'route_name']

class BusLocationSerializer(serializers.ModelSerializer):
    bus = BusSerializer(read_only=True)

    class Meta:
        model = BusLocation
        fields = ['id', 'bus', 'latitude', 'longitude', 'timestamp']
