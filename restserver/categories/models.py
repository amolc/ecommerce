from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly define 'id' as the primary key (AutoField is default for auto-increment)
    category_name = models.CharField(max_length=100, unique=True)  # Category name, unique to avoid duplicates
    category_description = models.TextField(blank=True, null=True)  # Optional field for additional details
    org_id = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set on category creation
    updated_at = models.DateTimeField(auto_now=True)      # Auto-updates on category edit
    is_active = models.BooleanField(default=True)         # Active status for category visibility

    def __str__(self):
        return self.category_name
