from django.db import models
from django.utils.timezone import now

class eventdata(models.Model):
    org_id = models.IntegerField()
    title = models.CharField(max_length=255)
    organizer_name = models.CharField(max_length=255)  # Changed from 'organizer' to 'organizer_name'
    start_date = models.DateField(default=now)  
    end_date = models.DateField(default=now)
    start_time = models.TimeField(default="00:00:00")
    end_time = models.TimeField(default="00:00:00")
    location = models.CharField(max_length=255, default="Add location")
    address1 = models.CharField(max_length=255, default="Add address1")
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, default="Add city")
    state = models.CharField(max_length=255, default="Add state")
    country = models.CharField(max_length=255, default="Add country")  # Added country field with default value
    postalcode = models.CharField(max_length=20, default="000000")  # Added postalcode field with default value
    facebook = models.CharField(max_length=255, blank=True, null=True)  # Added facebook field
    image1 = models.TextField(blank=True, null=True)  # Image as text field (URL or base64)
    image2 = models.TextField(blank=True, null=True)  # Additional images
    image3 = models.TextField(blank=True, null=True)  # Additional images
    contactname = models.CharField(max_length=255, default="Add contact name")  # Contact person name
    contactnumber = models.CharField(max_length=20, default="Add contact number")  # Contact person number
    description = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)  # Tags for the event
    category = models.CharField(max_length=100, default="Add category")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "eventdata"
