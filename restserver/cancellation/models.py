from django.db import models

# Create your models here.
class Cancellation(models.Model):
    org_id = models.PositiveIntegerField(null=True, blank=True)  # Organization ID
    booking_reference = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=15)
    reason = models.TextField()

    class Meta:
        db_table = "cancellations"

    def __str__(self):
        return f"Cancellation for {self.booking_reference} by {self.name}"
