from typing import (
    Any,
)

from django.db import models
from products.models import Product
from django.utils import timezone

from organisations.models import (
    Organisation
)


class Inventory(models.Model):
    id: models.AutoField = models.AutoField(
        primary_key=True,
    )
    stock_quantity: models.PositiveIntegerField = models.PositiveIntegerField(
        default=0
    )
    minimum_stock_level: models.PositiveIntegerField = models.PositiveIntegerField(  # noqa: E501
        default=10
    )
    last_restock_date: models.DateTimeField = models.DateTimeField(
        blank=True,
        null=True
    )
    restock_quantity: models.PositiveIntegerField = models.PositiveIntegerField(  # noqa: E501
        blank=True,
        null=True
    )
    notes: models.TextField = models.TextField(
        blank=True,
        null=True
    )

    product: models.OneToOneField = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='inventory'
    )
    created_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True
    )
    updated_at: models.DateTimeField = models.DateTimeField(
        auto_now=True
    )

    organisation: models.ForeignKey = models.ForeignKey(
        Organisation,
        on_delete=models.DO_NOTHING,
        related_name="organisation",
    )
  
    def __str__(self):
        return f"Inventory for {self.product.product_name}"

    def is_below_minimum(self):
        """Check if the stock is below the minimum stock level."""
        return self.stock_quantity < self.minimum_stock_level

    def restock(self, quantity: float):
        """
        Update stock level when new stock is added.
        :param quantity: Number of units to add to stock.
        """
        self.stock_quantity += quantity
        self.last_restock_date = timezone.now()
        self.restock_quantity = quantity
        self.save()


class StockMovement(models.Model):
    """
    Tracks stock movements for inventory (e.g., stock in/out events).
    """
    MOVEMENT_CHOICES = [
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
    ]

    product: models.ForeignKey = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='stock_movements'
    )
    movement_type: models.CharField = models.CharField(
        max_length=3,
        choices=MOVEMENT_CHOICES
    )
    quantity: models.PositiveIntegerField = models.PositiveIntegerField()
    timestamp: models.DateTimeField = models.DateTimeField(
        auto_now_add=True
    )
    note: models.TextField = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return (
            f"{self.movement_type} {self.quantity} "
            f"for {self.product.product_name}"
        )

    def save(self, *args: Any, **kwargs: Any):
        """
        Adjust inventory stock levels upon save.
        """
        inventory = self.product.inventory  # type: ignore
        if self.movement_type == 'IN':
            inventory.stock_quantity += self.quantity
        elif self.movement_type == 'OUT':
            if inventory.stock_quantity < self.quantity:
                raise ValueError(
                    "Insufficient stock to complete this operation."
                )
            inventory.stock_quantity -= self.quantity
        inventory.save()
        super().save(*args, **kwargs)
