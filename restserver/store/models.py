from django.db import models

# Create your models here.
from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Store Name")
    address1 = models.TextField(verbose_name="Address Line 1")
    address2 = models.TextField(blank=True, null=True, verbose_name="Address Line 2")
    address3 = models.TextField(blank=True, null=True, verbose_name="Address Line 3")
    
    def __str__(self):
        return self.name
