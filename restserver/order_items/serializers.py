from rest_framework import serializers  # type: ignore
from .models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            'product',
            'product_name',
            'product_qty',
            'product_price',
            'product_subtotal'
        ]
