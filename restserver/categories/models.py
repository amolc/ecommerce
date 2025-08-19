from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=150)
    category_description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name
