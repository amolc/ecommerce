from django.db import models

# Create your models here.
class Enquiry(models.Model):
    NEW_BOOKING = 'New Booking'
    EXISTING_BOOKING = 'Existing Booking'
    UPCOMING_BOOKING = 'Upcoming Booking'

    CONCERN_CHOICES = [
        (NEW_BOOKING, 'New Booking'),
        (EXISTING_BOOKING, 'Existing Booking'),
        (UPCOMING_BOOKING, 'Upcoming Booking'),
    ]

    org_id = models.PositiveIntegerField(null=True, blank=True)  # Organization ID
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=15)
    concern = models.CharField(max_length=50, choices=CONCERN_CHOICES)
    property_location = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        db_table = "enquiries"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.concern}"
