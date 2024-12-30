from django.db import models


class Order(models.Model):
    order_id: models.AutoField = models.AutoField(
        primary_key=True
    )
    first_name: models.CharField = models.CharField(
        max_length=50
    )
    last_name: models.CharField = models.CharField(
        max_length=50
    )
    email: models.EmailField = models.EmailField(
        blank=True,
        null=True
    )
    mobile_number: models.CharField = models.CharField(
        max_length=15
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
    org_id: models.PositiveIntegerField = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    billing_address: models.TextField = models.TextField()
    shipping_address: models.TextField = models.TextField(
        blank=True,
        null=True
    )

    status: models.CharField = models.CharField(
        max_length=20,
        default='pending',
        choices=(
            ('pending', 'Pending'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled'),
        )
    )

    amount: models.DecimalField = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_method: models.CharField = models.CharField(
        max_length=20,
        default='credit_card',
        choices=(
            ('credit_card', 'Credit Cart'),
            ('mobile_money', 'Mobile Money')
        )
    )

    created_on: models.DateTimeField = models.DateTimeField(
        auto_now_add=True
    )

    updated_on: models.DateTimeField = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return (
            f"Order {self.order_id} - {self.first_name} "
            f"{self.last_name} - {self.order_status}"
        )
