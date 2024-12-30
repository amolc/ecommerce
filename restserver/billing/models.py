from django.db import models


class Billing(models.Model):
    first_name: models.CharField = models.CharField(
        max_length=255
    )
    last_name: models.CharField = models.CharField(
        max_length=255
    )
    email: models.EmailField = models.EmailField(
        max_length=255,
        unique=True
    )
    mobile_number: models.CharField = models.CharField(
        max_length=15
    )
    country: models.CharField = models.CharField(
        max_length=100
    )
    state: models.CharField = models.CharField(
        max_length=100
    )
    city: models.CharField = models.CharField(
        max_length=255
    )
    postal_code: models.CharField = models.CharField(
        max_length=20
    )

    org_id: models.PositiveIntegerField = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    billing_address: models.TextField = models.TextField()
    billing_date: models.DateTimeField = models.DateTimeField(
        auto_now_add=True
    )
    total_amount: models.DecimalField = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    is_paid: models.BooleanField = models.BooleanField(
        default=False
    )

    def __str__(self):
        return (
            f"Billing {self.id} - {self.first_name} {self.last_name}"
            f"- {'Paid' if self.is_paid else 'Unpaid'}"
        )
