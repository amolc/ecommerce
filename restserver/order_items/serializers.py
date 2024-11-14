from rest_framework import serializers
from .models import OrderItems

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = '__all__' 