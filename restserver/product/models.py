from django.db import models
from categories.models import Category
from subcategories.models import Subcategory  # Corrected the import to use the proper model class name

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)  # Product name
    product_description = models.TextField(blank=True, null=True)  # Product description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product
    stock_quantity = models.PositiveIntegerField(default=0)  # Stock quantity available
    org_id = models.PositiveIntegerField(blank=True, null=True)  # Organization ID
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', default=1)  # ForeignKey to Category
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='products', default=1)  # ForeignKey to Subcategory

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)  # Is the product active?

    def __str__(self):
        return self.product_name  # Corrected to return the product_name
