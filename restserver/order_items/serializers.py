from rest_framework import serializers  # type: ignore
from .models import OrderItem


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

        def __init__(self, *args, **kwargs):
            request = kwargs.get('context', {}).get(
                'request',
                None
            )

            super(OrderItemSerializer, self).__init__(
                *args,
                **kwargs
            )

            if request and request.method == 'GET':
                self.Meta.depth = 2
            else:
                self.Meta.depth = 0
