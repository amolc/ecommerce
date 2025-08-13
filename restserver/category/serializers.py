from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    organisation_name = serializers.CharField(
        source='organisation.name',
        read_only=True
    )

    class Meta:
        model = Category
        fields = [
            'id',
            'category_name',
            'category_description',
            'is_active',
            'category_image',
            'created_at',
            'updated_at',
            'organisation',
            'organisation_name'
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at'
        ]
        extra_kwargs = {
            'category_name': {'required': True},
            'category_description': {'required': True},
            'is_active': {'required': True},
            'category_image': {'required': True}
        }
