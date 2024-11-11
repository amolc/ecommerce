from rest_framework import serializers
from .models import PropertyManager

class PropertyManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyManager
        fields = '__all__'
