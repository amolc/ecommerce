from rest_framework import serializers
from .models import Subcategory
# from categories.models import Category


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'subcategory_name', 'subcategory_description', 'org_id', 'category', 'created_at', 'updated_at', 'is_active']


# class SubcategorySerializer(serializers.ModelSerializer):
#     # Include the related category's name in the serializer
#     category_name = serializers.CharField(source='category.name', read_only=True)
#     category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)

#     class Meta:
#         model = Subcategory
#         fields = ['id', 'subcategory_name', 'subcategory_description', 'category_name', 'category_id', 'is_active', 'created_at', 'updated_at']

#     def create(self, validated_data):
#         # Create a new subcategory with the validated data
#         category = validated_data.pop('category')  # Get the category object from the data
#         subcategory = Subcategory.objects.create(category=category, **validated_data)
#         return subcategory

#     def update(self, instance, validated_data):
#         # Update an existing subcategory with the validated data
#         category = validated_data.pop('category', None)  # Get the category if provided

#         if category:
#             instance.category = category

#         instance.subcategory_name = validated_data.get('subcategory_name', instance.subcategory_name)
#         instance.subcategory_description = validated_data.get('subcategory_description', instance.subcategory_description)
#         instance.is_active = validated_data.get('is_active', instance.is_active)
#         instance.save()
#         return instance
