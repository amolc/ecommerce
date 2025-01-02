from django.db import (
    models
)
from django.core.exceptions import (
    ValidationError
)


class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    id: models.AutoField = models.AutoField(
        primary_key=True
    )
    org_id: models.PositiveIntegerField = models.PositiveIntegerField(
        blank=True,
        null=True
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

    def save(self, *args, **kwargs):
        if self.pk:
            original_order = Order.objects.get(
                pk=self.pk
            )

            if original_order.status != self.status:
                if (
                    original_order.status == 'pending'
                    and self.status in ['completed', 'cancelled']
                ):
                    super().save(*args, **kwargs)

                    OrderStatusChange.objects.create(
                        order=self,
                        status_from=original_order.status,
                        status_to=self.status
                    )
                    return
                else:
                    raise ValidationError(
                        "Status can only be changed from "
                        "'pending' to 'completed' or 'cancelled'"
                    )

        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"Order {self.id} - {self.first_name} "
            f"{self.last_name} - {self.status}"
        )


class OrderStatusChange(models.Model):
    order: models.ForeignKey = models.ForeignKey(
        Order,
        on_delete=models.DO_NOTHING,
        related_name='status_changes'
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

    def __str__(self):
        return (
            f"Status changed from: {self.status_from} "
            f"to {self.status_to} for order "
            f"{self.order} on {self.created_on}"
        )
