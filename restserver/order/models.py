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
    org_id: models.PositiveIntegerField = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    billing_address: models.TextField = models.TextField()
    shipping_address: models.TextField = models.TextField()
    order_date: models.DateTimeField = models.DateTimeField(
        auto_now_add=True
    )

    order_status: models.CharField = models.CharField(
        max_length=20,
        default='Pending'
    )
    order_amount: models.DecimalField = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    order_paid_by: models.CharField = models.CharField(
        max_length=20,
        default='Credit Card'
    )

    def __str__(self):
        return (
            f"Order {self.order_id} - {self.first_name} "
            f"{self.last_name} - {self.order_status}"
        )
