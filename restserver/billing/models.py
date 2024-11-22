from django.db import models
from customers.models import Customers  


class Billing(models.Model):
    # Customer-specific fields
    first_name = models.CharField(max_length=255)  # Customer's first name
    last_name = models.CharField(max_length=255)  # Customer's last name
    email = models.EmailField(max_length=255, unique=True)  # Customer's email (unique constraint ensures no duplicates)
    city = models.CharField(max_length=255)  # Customer's city
    mobile_number = models.CharField(max_length=15)  # Customer's mobile number
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, null=True, blank=True)  # Temporarily allow null

    # Billing-specific fields
    org_id = models.PositiveIntegerField(null=True, blank=True)  # Optional org ID
    billing_address = models.TextField()  # Full billing address
    state = models.CharField(max_length=100)  # State of the billing address
    postal_code = models.CharField(max_length=20)  # Postal/ZIP code
    country = models.CharField(max_length=100)  # Country of the billing address
    billing_date = models.DateTimeField(auto_now_add=True)  # Date when the billing was created
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total billed amount
    is_paid = models.BooleanField(default=False)  # Payment status

    def __str__(self):
        return f"Billing {self.id} - {self.first_name} {self.last_name} - {'Paid' if self.is_paid else 'Unpaid'}"
