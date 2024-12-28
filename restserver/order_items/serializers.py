from rest_framework import serializers
from .models import OrderItems

class OrderItemSerializer(serializers.ModelSerializer):
   class Meta:
        model = OrderItems
        fields = [
            'id',  # ID of the order item
            'org_id',  # Organization ID
            'order',  # ForeignKey reference to Order
            'product_name',  # Product name
            'product_qty',  # Quantity of the product
            'product_price',  # Price per unit of the product
            'product_subtotal'  # Subtotal for the product (product_qty * product_price)
        ]