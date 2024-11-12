from rest_framework import serializers
from .models import Subcategory
from categories.models import Category

class SubcategorySerializer(serializers.ModelSerializer):
    # Including category details in the serializer
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Subcategory
        fields = '__all__'  
        
    def create(self, validated_data):
        # Create a new subcategory with the validated data
        subcategory_name = validated_data.get('subcategory_name')
        subcategory_description = validated_data.get('subcategory_description')
        is_active = validated_data.get('is_active', True)

        # Create a Subcategory object
        subcategory = Subcategory.objects.create(
            subcategory_name=subcategory_name,
            subcategory_description=subcategory_description,
            is_active=is_active
        )
        return subcategory

    def update(self, instance, validated_data):
        # Update an existing subcategory with the validated data
        instance.subcategory_name = validated_data.get('subcategory_name', instance.subcategory_name)
        instance.subcategory_description = validated_data.get('subcategory_description', instance.subcategory_description)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance
