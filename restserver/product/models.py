from django.db import models
from categories.models import Category
from subcategories.models import Subcategory  # Corrected the import to use the proper model class name
from datetime import date

# Create your models here.
class Products(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)  # Product name
    product_description = models.TextField(blank=True, null=True)  # Product description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Discounted price
    unit = models.CharField(max_length=50, blank=True, null=True)  # Unit of measurement (e.g., kg, lb, piece)
    stock_quantity = models.PositiveIntegerField(default=0)  # Stock quantity available
    org_id = models.PositiveIntegerField(blank=True, null=True)  # Organization ID
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', default=1)  # ForeignKey to Category
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='products', default=1)  # ForeignKey to Subcategory
    
    mfg = models.DateField(default=date.today)
    product_life = models.PositiveIntegerField(default=1)  # Product life in days
    product_image1 = models.TextField(blank=True, null=True)  # First product image path
    product_image2 = models.TextField(blank=True, null=True)  # Second product image path
    availability = models.BooleanField(default=True)  # Boolean indicating availability
    product_type = models.CharField(
        max_length=20, 
        choices=[
            ('veg', 'Vegetarian'),
            ('nonveg', 'Non-Vegetarian'),
            ('organic', 'Organic'),
            ('non-organic', 'Non-Organic')
        ],
        default='organic'
    )  # Product type (veg, nonveg, organic, non-organic)


    category_name = models.TextField(blank=True, null=True)
    subcategory_name = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp when created
    updated_at = models.DateTimeField(auto_now=True)  # Auto timestamp when updated
    is_active = models.BooleanField(default=True)  # Is the product active?

    def __str__(self):
        return self.product_name