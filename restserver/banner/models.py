from django.db import models


class Banner(models.Model):
    background_image: models.ImageField = models.ImageField()
    title: models.CharField = models.CharField(
        max_length=255
    )
    subtitle: models.CharField = models.CharField(
        max_length=255
    )

    def __str__(self):
        return (
            f"{self.title}-"
            f"{self.subtitle}"
        )
