from django.db import models
from django.contrib.postgres.fields import ArrayField  # type: ignore

# Create your models here.
class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('Villa', 'Villa'),
        ('Bungalow', 'Bungalow'),
        ('Hotel', 'Hotel'),
    ]
    
    GREAT_FOR_CHOICES = [
        ('Senior_Citizen', 'Senior_Citizen'),
        ('Kids', 'Kids'),
        ('Adults', 'Adults'),
        ('All', 'All'),
        ('Others', 'Others'),
    ]

    org_id = models.PositiveIntegerField()
    property_name = models.CharField(max_length=100)
    property_key_name = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    city = models.CharField(max_length=50)  # Increased length
    state = models.CharField(max_length=50)  # Increased length
    cost_per_night = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # New fields
    title = models.CharField(max_length=255, default='Add Title')
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPE_CHOICES, default='Select Property Type')
    price_villa = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_room = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    num_rooms = models.PositiveIntegerField(default=0)
    description = models.TextField(default='No description available')
    floors = models.PositiveIntegerField(default=0)
    num_bedrooms = models.PositiveIntegerField(default=0)
    num_bathrooms = models.PositiveIntegerField(default=0)
    guest_limit = models.PositiveIntegerField(default=0)
    meals_available = models.TextField(null=True, blank=True)
    
    # Bedroom image URLs
    bedroom1_image = models.TextField(null=True, blank=True)
    description1 = models.TextField(default='')
    bedroom2_image = models.TextField(null=True, blank=True)
    description2 = models.TextField(default='')
    bedroom3_image = models.TextField(null=True, blank=True)
    description3 = models.TextField(default='')
    bedroom4_image = models.TextField(null=True, blank=True)
    description4 = models.TextField(default='')
    total_bedroom_size = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    square_feet = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    location_url = models.TextField(null=True, blank=True)
    video_url = models.TextField(null=True, blank=True)
    great_for = models.CharField(max_length=50, choices=GREAT_FOR_CHOICES, default='all')
    other_images = models.TextField(null=True, blank=True)
    img = models.TextField(null=True, blank=True)
    img3 = models.TextField(null=True, blank=True)
    address1 = models.CharField(max_length=100, default='Unknown')
    address2 = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=20, default='Enter Pincode')
    amenities = ArrayField(models.CharField(max_length=50), blank=True, default=list)
    best_rated = models.BooleanField(default=False)
    most_loved = models.BooleanField(default=False)
    agent_id = models.PositiveIntegerField(default=1)

    room_name_1 = models.CharField(max_length=100, null=True, blank=True)
    room_name_1_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    room_name_2 = models.CharField(max_length=100, null=True, blank=True)
    room_name_2_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    room_name_3 = models.CharField(max_length=100, null=True, blank=True)
    room_name_3_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    room_name_4 = models.CharField(max_length=100, null=True, blank=True)
    room_name_4_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(default=0)
    updated_date = models.DateTimeField(null=True)
    updated_by = models.IntegerField(default=0)

    class Meta:
        db_table = "Property"

    def __str__(self):
        return self.property_name
        

class PropertyImages(models.Model):
    property_id = models.ForeignKey('Property', on_delete=models.RESTRICT, related_name='propertyImage',)
    image = models.ImageField(upload_to='property/image')
    
    def __str__(self):
        return f"Image for Property ID {self.property_id.id}"