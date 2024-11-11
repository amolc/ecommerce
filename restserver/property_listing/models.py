from django.db import models

class PropertyListing(models.Model):
    VILLA = 'Villa'
    COTTAGE = 'Cottage'
    BUNGALOW = 'Bungalow'
    UNDER_CONSTRUCTION = 'Under Construction'

    PROPERTY_TYPE_CHOICES = [
        (VILLA, 'Villa'),
        (COTTAGE, 'Cottage'),
        (BUNGALOW, 'Bungalow'),
        (UNDER_CONSTRUCTION, 'Under Construction'),
    ]

    FACEBOOK = 'Facebook'
    INSTAGRAM = 'Instagram'
    GSEARCH = 'Google Search'
    REFERENCE_GUEST = 'Reference from Guest'
    REFERENCE_OWNER = 'Reference from Property Owner'
    BLOGS = 'Blogs'

    HEARD_FROM_CHOICES = [
        (FACEBOOK, 'Facebook'),
        (INSTAGRAM, 'Instagram'),
        (GSEARCH, 'Google Search'),
        (REFERENCE_GUEST, 'Reference from Guest'),
        (REFERENCE_OWNER, 'Reference from Property Owner'),
        (BLOGS, 'Blogs'),
    ]

    org_id = models.PositiveIntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=15)
    property_location = models.CharField(max_length=255)
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPE_CHOICES)
    num_rooms = models.PositiveIntegerField()
    heard_from = models.CharField(max_length=50, choices=HEARD_FROM_CHOICES)
    photo_website = models.URLField(blank=True, null=True)
    property_description = models.TextField()
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    class Meta:
        db_table = "property_listings"

    def __str__(self):
        return f"{self.property_type} - {self.property_location} ({self.first_name} {self.last_name})"
