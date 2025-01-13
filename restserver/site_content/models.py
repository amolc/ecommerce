from django.db import models

from organisations.models import (
    Organisation
)


class Banner(models.Model):
    background_image: models.ImageField = models.ImageField()
    title: models.CharField = models.CharField(
        max_length=255
    )
    subtitle: models.CharField = models.CharField(
        max_length=255
    )
    created_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at: models.DateTimeField = models.DateTimeField(
        auto_now=True,
    )

    organisation: models.OneToOneField = models.ForeignKey(
        Organisation,
        on_delete=models.DO_NOTHING,
        related_name="banner",
    )

    def __str__(self):
        return (
            f"{self.title}-"
            f"{self.subtitle}"
        )
