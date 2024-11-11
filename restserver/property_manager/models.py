from django.db import models

# Create your models here.
class PropertyManager(models.Model):
    org_id = models.PositiveIntegerField(null=True, blank=True)
    manager_name = models.CharField(max_length=255)
    manager_email = models.EmailField(unique=True)
    manager_phone = models.CharField(max_length=20)
    availability_status = models.BooleanField(default=True)
    date_of_hire = models.DateTimeField()
    total_properties_managed = models.IntegerField(default=0)
    address = models.CharField(max_length=255)
    
    def __str__(self):
        return self.manager_name
