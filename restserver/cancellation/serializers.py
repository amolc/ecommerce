from rest_framework import serializers
from .models import Cancellation

class CancellationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancellation
        fields = '__all__'
