from django.db import models

class Destination(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    img = models.URLField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'Destination'
