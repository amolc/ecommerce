from rest_framework import serializers  # type: ignore
from .models import (
    Product,
    ProductCategory,
    ProductSubcategory
)


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductSubcategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source='category.category_name',
        read_only=True
    )

    class Meta:
        model = ProductSubcategory
        fields = [
            'id',
            'subcategory_name',
            'category_name',
            'subcategory_description',
            'category',
            'created_at',
            'updated_at',
            'is_active'
        ]


class ProductSerializer(serializers.ModelSerializer):
    category_name: serializers.CharField = serializers.CharField(
        source='category.category_name',
        read_only=True
    )

    subcategory_name: serializers.CharField = serializers.CharField(
        source='subcategory.subcategory_name',
        read_only=True
    )

    class Meta:
        model = Product
        fields = '__all__'
