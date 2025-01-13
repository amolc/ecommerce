from django.db import models


class Organisation(models.Model):
    name: models.CharField = models.CharField(
        max_length=255
    )
    
    def __str__(self):
        return (
            f"{self.name}"
        )
