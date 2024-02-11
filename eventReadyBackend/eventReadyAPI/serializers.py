from rest_framework import serializers
from .models import * 

class EventSerializer(serializers.ModelSerializer):
    class Meta: 
        model = EventGeneralInfo
        fields = ('id', 'name', 'doe', 'start_time', 'end_time', 'location', 'description', 'created', 'active')