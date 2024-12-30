from rest_framework import serializers  # type: ignore
from .models import Product


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
