from rest_framework import serializers  # type: ignore

from django.db import (
    transaction
)

from order_items.models import (
    OrderItem
)

from order_items.serializers import (
    OrderItemSerializer
)

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(
        many=True
    )

    class Meta:
        model = Order
        fields = [
            'first_name',
            'last_name',
            'email',
            'mobile_number',
            'country',
            'state',
            'city',
            'billing_address',
            'shipping_address',
            'amount',
            'order_items',
        ]

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')

        with transaction.atomic():
            order = Order.objects.create(**validated_data)

            for item_data in order_items_data:
                OrderItem.objects.create(
                    order=order,
                    **item_data
                )

        return order

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
