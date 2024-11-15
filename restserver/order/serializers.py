from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'order_id', 
            'first_name', 
            'last_name', 
            'billing_address', 
            'shipping_address', 
            'order_date', 
            'order_status', 
            'order_amount', 
            'order_paid_by'
        ]
