from django.db import models
from organisations.models import Organisation

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'product_categories'

    id: models.AutoField = models.AutoField(
        primary_key=True
    )
    category_name: models.CharField = models.CharField(
        max_length=100,
        unique=True,
    )
    category_description: models.TextField = models.TextField(
        blank=True,
        null=True
    )
    is_active: models.BooleanField = models.BooleanField(
        default=True
    )
    # Changed from ImageField → TextField
    category_image: models.TextField = models.TextField(
        null=True,
        blank=True,
        help_text="Store image URL, path, or Base64 text"
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
        related_name="categories",
    )

    def __str__(self):
        return self.category_name
