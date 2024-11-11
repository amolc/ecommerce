from rest_framework import serializers
from .models import eventdata

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = eventdata
        fields = '__all__'
