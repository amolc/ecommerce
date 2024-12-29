from django.db import models


class Category(models.Model):
    id: models.AutoField = models.AutoField(
        primary_key=True
    )
    # Explicitly define 'id' as the primary key
    #  (AutoField is default for auto-increment)

    category_name: models.CharField = models.CharField(
        max_length=100
    )  # Category name, unique to avoid duplicates
    category_description: models.TextField = models.TextField(
        blank=True,
        null=True
    )  # Optional field for additional details
    org_id: models.PositiveIntegerField = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    created_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True
    )  # Auto-set on category creation
    updated_at: models.DateTimeField = models.DateTimeField(
        auto_now=True
    )  # Auto-updates on category edit
    is_active: models.BooleanField = models.BooleanField(
        default=True
    )  # Active status for category visibility
    category_image: models.TextField = models.TextField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'
