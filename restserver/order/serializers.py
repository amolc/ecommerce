from rest_framework import serializers
from .models import Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__' 