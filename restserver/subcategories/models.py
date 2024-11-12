from django.db import models
from categories.models import Category

# Create your models here.
class Subcategory(models.Model):
    subcategory_name = models.CharField(max_length=100)  # Name of the subcategory
    subcategory_description = models.TextField(blank=True, null=True)  # Optional field
    created_at = models.DateTimeField(auto_now_add=True)
    org_id = models.IntegerField(blank=True, null=True)  # Simple integer field for org_id
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories', default=1)

    def __str__(self):
        return self.subcategory_name  # Corrected to return subcategory_name

