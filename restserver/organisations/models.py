from django.db import models


class Organisation(models.Model):
    id: models.AutoField = models.AutoField(
        primary_key=True
    )
    name: models.CharField = models.CharField(
        max_length=255,
        unique=True,
    )
    display_name: models.CharField = models.CharField(
        max_length=255,
        unique=True,
    )
    created_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True
    )
    updated_at: models.DateTimeField = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return (
            f"{self.name}"
        )
