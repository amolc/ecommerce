from rest_framework import serializers  # type: ignore
from .models import (
    Category,
    Subcategory
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubcategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source='category.category_name',
        read_only=True
    )

    class Meta:
        model = Subcategory
        fields = [
            'id',
            'subcategory_name',
            'category_name',
            'subcategory_description',
            'org_id',
            'category',
            'created_at',
            'updated_at',
            'is_active'
        ]
