# django
from rest_framework import serializers

# custom
from .models import Property, PropertyImages


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'id', 'org_id', 'property_name', 'property_key_name', 'is_active', 'city', 
            'state', 'cost_per_night', 'title', 'property_type', 'price_room', 'price_villa', 'num_rooms', 'description', 
            'floors', 'num_bedrooms', 'num_bathrooms', 'guest_limit', 'meals_available',
            'bedroom1_image', 'description1', 'bedroom2_image', 'description2',
            'bedroom3_image', 'description3', 'bedroom4_image', 'description4',
            'total_bedroom_size', 'square_feet', 'location_url', 'video_url', 'great_for', 'best_rated', 'most_loved',
            'other_images', 'img','img3','room_name_1','room_name_1_cost','room_name_2','room_name_2_cost','room_name_3','room_name_3_cost','room_name_4','room_name_4_cost', 'address1', 'address2', 'pincode', 'amenities','agent_id',
            'created_date', 'created_by', 'updated_date', 'updated_by'
        ]
        read_only_fields = ['id', 'created_date', 'created_by', 'updated_date', 'updated_by']
        
class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImages
        fields = '__all__'
        extra_kwargs = {
            'image': {'required': True}  # Ensures the image field is required
        }