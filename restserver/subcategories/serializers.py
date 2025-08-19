from rest_framework import serializers
from .models import Subcategory

class SubcategorySerializer(serializers.ModelSerializer):
    # If you want category name read-only, uncomment the next line and add to fields
    # category_name = serializers.CharField(source='category.category_name', read_only=True)

    class Meta:
        model = Subcategory
        fields = ['id', 'subcategory_name', 'subcategory_description', 'category']
