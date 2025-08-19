from django.db import models
from organisations.models import Organisation  # assuming you already have this

class Category(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Sub Categories"
        unique_together = ("category", "name")

    def __str__(self):
        return f"{self.category.name} → {self.name}"
