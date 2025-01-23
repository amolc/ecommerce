from typing import (
    Any,
)

from django.db import (
    models
)
from django.core.exceptions import (
    ValidationError
)

from organisations.models import (
    Organisation
)

from products.models import (
    Product
)

from customers.models import (
    Customer
)


class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('ready_for_delivery', 'Ready for Delivery'),
        ('goods_collected', 'Goods Collected'),
        ('delivered', 'Delivered'),
    )
    PAYMENT_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )

    id: models.AutoField = models.AutoField(
        primary_key=True
    )
    email: models.EmailField = models.EmailField(
        blank=True,
        null=True
    )
    mobile_number: models.CharField = models.CharField(
        max_length=15
    )
    first_name: models.CharField = models.CharField(
        max_length=50
    )
    last_name: models.CharField = models.CharField(
        max_length=50
    )
    billing_address: models.TextField = models.TextField()
    billing_address_specifier: models.TextField = models.TextField(
        blank=True,
        null=True
    )
    billing_address2: models.TextField = models.TextField(
        blank=True,
        null=True
    )
    billing_address2_specifier: models.TextField = models.TextField(
        blank=True,
        null=True
    )
    country: models.CharField = models.CharField(
        max_length=120
    )
    state: models.CharField = models.CharField(
        max_length=250
    )
    city: models.CharField = models.CharField(
        max_length=120,
    )
    postal_code: models.CharField = models.CharField(
        max_length=10
    )
    shipping_email: models.EmailField = models.EmailField(
        blank=True,
        null=True
    )
    shipping_mobile_number: models.CharField = models.CharField(
        max_length=15
    )
    shipping_first_name: models.CharField = models.CharField(
        max_length=50
    )
    shipping_last_name: models.CharField = models.CharField(
        max_length=50
    )
    shipping_address: models.TextField = models.TextField()
    shipping_address_specifier: models.TextField = models.TextField(
        blank=True,
        null=True
    )
    shipping_address2: models.TextField = models.TextField(
        blank=True,
        null=True
    )
    shipping_address2_specifier: models.TextField = models.TextField(
        blank=True,
        null=True
    )
    shipping_country: models.CharField = models.CharField(
        max_length=120
    )
    shipping_state: models.CharField = models.CharField(
        max_length=250
    )
    shipping_city: models.CharField = models.CharField(
        max_length=120,
    )
    shipping_postal_code: models.CharField = models.CharField(
        max_length=10
    )

    status: models.CharField = models.CharField(
        max_length=20,
        default='pending',
        choices=STATUS_CHOICES
    )

    amount: models.DecimalField = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    payment_method: models.CharField = models.CharField(
        max_length=50,
        choices=PAYMENT_STATUS_CHOICES,
        default='upi'
    )
    payment_status: models.CharField = models.CharField(
        max_length=50,
        choices=PAYMENT_STATUS_CHOICES,
        default='pending',
    )
    created_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True
    )
    updated_at: models.DateTimeField = models.DateTimeField(
        auto_now=True
    )

    organisation: models.ForeignKey = models.ForeignKey(
        Organisation,
        on_delete=models.DO_NOTHING,
        related_name="orders"
    )
    customer: models.ForeignKey = models.ForeignKey(
        Customer,
        on_delete=models.DO_NOTHING,
        related_name="orders"
    )

    def save(self, *args: Any, **kwargs: Any):
        if self.pk:
            original_order = Order.objects.get(
                pk=self.pk
            )

            if original_order.status != self.status:
                valid_transitions = {
                    'pending': ['confirmed'],
                    'confirmed': ['ready_for_delivery'],
                    'ready_for_delivery': ['goods_collected', 'delivered'],
                    'goods_collected': [],
                    'delivered': []
                }

                if self.status not in valid_transitions[original_order.status]:
                    raise ValidationError(
                        f"Invalid status transition from {original_order.status} to {self.status}"
                    )

                super().save(*args, **kwargs)

                OrderStatusChange.objects.create(
                    order=self,
                    status_from=original_order.status,
                    status_to=self.status
                )
                return

        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"Order {self.id} - {self.first_name} "
            f"{self.last_name} - {self.status}"
        )


class OrderPaymentStatusChange(models.Model):
    id: models.AutoField = models.AutoField(
        primary_key=True,
    )
    status_from: models.CharField = models.CharField(
        max_length=255,
        choices=Order.PAYMENT_STATUS_CHOICES
    )
    status_to: models.CharField = models.CharField(
        max_length=255,
        choices=Order.PAYMENT_STATUS_CHOICES
    )
    created_on: models.DateTimeField = models.DateTimeField(
        auto_now_add=True
    )
    updated_on: models.DateTimeField = models.DateTimeField(
        auto_now=True
    )

    order: models.ForeignKey = models.ForeignKey(
        "orders.order",
        on_delete=models.CASCADE,
        related_name='payment_status_changes'
    )

    def __str__(self):
        return (
            f"Status changed from: {self.status_from} "
            f"to {self.status_to} for order "
            f"{self.order} on {self.created_on}"
        )


class OrderStatusChange(models.Model):
    id: models.AutoField = models.AutoField(
        primary_key=True,
    )
    status_from: models.CharField = models.CharField(
        max_length=255,
        choices=Order.STATUS_CHOICES
    )
    status_to: models.CharField = models.CharField(
        max_length=255,
        choices=Order.STATUS_CHOICES
    )
    created_on: models.DateTimeField = models.DateTimeField(
        auto_now_add=True
    )
    updated_on: models.DateTimeField = models.DateTimeField(
        auto_now=True
    )

    order: models.ForeignKey = models.ForeignKey(
        Order,
        on_delete=models.DO_NOTHING,
        related_name='status_changes'
    )

    def __str__(self):
        return (
            f"Status changed from: {self.status_from} "
            f"to {self.status_to} for order "
            f"{self.order} on {self.created_on}"
        )


class OrderItem(models.Model):
    id: models.AutoField = models.AutoField(
        primary_key=True
    )
    org_id: models.PositiveIntegerField = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    product: models.ForeignKey = models.ForeignKey(
        Product,
        on_delete=models.DO_NOTHING,
        related_name="order_items",
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

    order: models.ForeignKey = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_items',
    )

    def __str__(self):
        return f"{self.product_name} (Order ID: {self.order.id})"
