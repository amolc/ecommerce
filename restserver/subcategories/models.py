from django.db import models
from categories.models import Category

class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=150)
    subcategory_description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return f"{self.subcategory_name} ({self.category.category_name})"
