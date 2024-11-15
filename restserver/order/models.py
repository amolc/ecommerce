from django.db import models

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)  # Unique order ID
    first_name = models.CharField(max_length=50)  # Customer's first name
    last_name = models.CharField(max_length=50)  # Customer's last name
    org_id = models.PositiveIntegerField(blank=True, null=True)
    billing_address = models.TextField()  # Billing address for the order
    shipping_address = models.TextField()  # Shipping address for the order
    order_date = models.DateTimeField(auto_now_add=True)  # Date and time of order creation

    order_status = models.CharField(
        max_length=20,
        default='Pending'
    )  # Status of the order
    
    order_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total order amount
    order_paid_by = models.CharField(
        max_length=20,
        default='Credit Card'
    )  # Payment method used

    def __str__(self):
        return f"Order {self.order_id} - {self.first_name} {self.last_name} - {self.order_status}"