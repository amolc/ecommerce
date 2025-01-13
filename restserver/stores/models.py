from django.db import models

from organisations.models import (
    Organisation
)


class Store(models.Model):
    id: models.AutoField = models.AutoField(
        primary_key=True,
    )
    name: models.CharField = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Store Name"
    )
    address1: models.TextField = models.TextField(
        verbose_name="Address Line 1"
    )
    address2: models.TextField = models.TextField(
        blank=True,
        null=True,
        verbose_name="Address Line 2"
    )
    address3: models.TextField = models.TextField(
        blank=True,
        null=True,
        verbose_name="Address Line 3"
    )
    created_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True
    )
    updated_at: models.DateTimeField = models.DateTimeField(
        auto_now=True
    )

    organisation: models.ForeignKey = models.ForeignKey(
        Organisation,
        on_delete=models.DO_NOTHING,
        related_name="stores",
    )

    def __str__(self):
        return self.name
