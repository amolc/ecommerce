from django.db import models
from order.models import Order
from product.models import (
    Product
)


class OrderItem(models.Model):
    id: models.AutoField = models.AutoField(
        primary_key=True
    )
    org_id: models.PositiveIntegerField = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    order: models.ForeignKey = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_items'
    )

    product: models.ForeignKey = models.ForeignKey(
        Product,
        on_delete=models.DO_NOTHING,
    )
    product_image: models.TextField = models.TextField()
    product_name: models.CharField = models.CharField(
        max_length=255
    )
    product_qty: models.PositiveIntegerField = models.PositiveIntegerField()
    product_price: models.DecimalField = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    is_discounted: models.BooleanField = models.BooleanField(
        default=False
    )
    product_subtotal: models.DecimalField = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.product_name} (Order ID: {self.order.id})"
