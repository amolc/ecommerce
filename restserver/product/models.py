from django.db import models
from categories.models import Category
from subcategories.models import Subcategory
from datetime import date


class Product(models.Model):
    id: models.AutoField = models.AutoField(
        primary_key=True
    )
    product_name: models.CharField = models.CharField(
        max_length=255
    )
    product_description: models.TextField = models.TextField(
        blank=True,
        null=True
    )
    price: models.DecimalField = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    discount_price: models.DecimalField = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    unit: models.CharField = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    stock_quantity: models.PositiveIntegerField = models.PositiveIntegerField(
        default=0
    )
    org_id: models.PositiveIntegerField = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    category: models.ForeignKey = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        default=1
    )
    subcategory: models.ForeignKey = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        related_name='products',
        default=1
    )
    mfg: models.DateField = models.DateField(
        default=date.today
    )
    product_life: models.PositiveIntegerField = models.PositiveIntegerField(
        default=1
    )
    product_image1: models.TextField = models.TextField(
        blank=True,
        null=True
    )
    product_image2: models.TextField = models.TextField(
        blank=True,
        null=True
    )
    availability: models.BooleanField = models.BooleanField(
        default=True
    )
    product_type: models.CharField = models.CharField(
        max_length=20,
        choices=[
            ('veg', 'Vegetarian'),
            ('nonveg', 'Non-Vegetarian'),
            ('organic', 'Organic'),
            ('non-organic', 'Non-Organic')
        ],
        default='organic'
    )
    category_name: models.TextField = models.TextField(
        blank=True,
        null=True
    )
    subcategory_name: models.TextField = models.TextField(
        blank=True,
        null=True
    )
    created_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True
    )
    updated_at: models.DateTimeField = models.DateTimeField(
        auto_now=True
    )
    is_active: models.BooleanField = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.product_name
