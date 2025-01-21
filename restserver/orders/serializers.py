from typing import (
    Dict,
    Any
)

from rest_framework import serializers  # type: ignore

from django.db import (
    transaction
)

from organisations.models import (
    Organisation
)

from customers.models import (
    Customer
)

from .models import (
    Order,
    OrderItem
)


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            'product',
            'product_name',
            'product_qty',
            'product_image',
            'product_price',
            'product_subtotal'
        ]


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(
        many=True
    )
    customer = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all()
    )
    organisation = serializers.PrimaryKeyRelatedField(
        queryset=Organisation.objects.all()
    )

    class Meta:
        model = Order
        fields = [
            'id',
            'email',
            'mobile_number',
            'first_name',
            'last_name',
            'billing_address',
            'billing_address_specifier',
            'billing_address2',
            'billing_address2_specifier',
            'country',
            'state',
            'city',
            'postal_code',
            'shipping_email',
            'shipping_mobile_number',
            'shipping_first_name',
            'shipping_last_name',
            'shipping_address',
            'shipping_address_specifier',
            'shipping_address2',
            'shipping_address2_specifier',
            'shipping_country',
            'shipping_state',
            'shipping_city',
            'shipping_postal_code',
            'amount',
            'order_items',
            'created_at',
            'updated_at',
            'status',
            'status_changes',
            'customer',
            'organisation',
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
            'status',
            'status_changes'
        ]
        depth = 2

    def __init__(self, *args: Any, **kwargs: Any):
        super(OrderSerializer, self).__init__(*args, **kwargs)

        request = self.context.get('request')
        if request and request.method == 'GET':
            self.fields['order_items'].depth = 2

    def create(self, validated_data: Dict[str, Any]):
        order_items_data = validated_data.pop('order_items')

        if len(order_items_data) == 0:
            raise Exception("There are no items in this order")

        with transaction.atomic():
            order = Order.objects.create(**validated_data)

            for item_data in order_items_data:
                OrderItem.objects.create(
                    order=order,
                    **item_data
                )
                
            customer = validated_data['customer'] 
 
            if 'billing_address' in validated_data:
                customer.billing_address = validated_data['billing_address']
            if 'billing_address_specifier' in validated_data:
                customer.billing_address_specifier = validated_data['billing_address_specifier']
            if 'billing_address2' in validated_data:
                customer.billing_address2 = validated_data['billing_address2']
            if 'billing_address2_specifier' in validated_data:
                customer.billing_address2_specifier = validated_data['billing_address2_specifier']
            if 'country' in validated_data:
                customer.country = validated_data['country']
            if 'city' in validated_data:
                customer.city = validated_data['city']
            if 'postal_code' in validated_data:
                customer.postal_code = validated_data['postal_code']

            customer.save()

        return order

    def update(self, instance: Order, validated_data: Dict[str, Any]):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
