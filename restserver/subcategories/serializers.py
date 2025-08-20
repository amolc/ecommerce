from rest_framework import serializers
from .models import SubCategory

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'subcategory_name', 'subcategory_description', 'is_active', 'category']
