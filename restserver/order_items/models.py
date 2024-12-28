from django.db import models
from order.models import Order

class OrderItems(models.Model):
    id = models.AutoField(primary_key=True)
    org_id = models.PositiveIntegerField(blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')  # Link to Order
    product_name = models.CharField(max_length=255)  # Name of the product
    product_qty = models.PositiveIntegerField()  # Quantity of the product ordered
    product_price = models.DecimalField(max_digits=10, decimal_places=2)  # Price per unit of the product
    product_subtotal = models.DecimalField(max_digits=10, decimal_places=2)  # Subtotal for this item (price * quantity)

    def __str__(self):
        return f"{self.product_name} (Order ID: {self.order.id})"
