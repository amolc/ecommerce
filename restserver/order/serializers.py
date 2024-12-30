from rest_framework import serializers  # type: ignore

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

    def update(self, instance, validated_data):
        """Override update method to handle partial updates"""
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
