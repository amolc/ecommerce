from typing import (
    Dict,
    Any
)
from rest_framework import (  # type: ignore
    serializers
)
from .models import Staff


class RegisterStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value: str):
        if not value:
            raise serializers.ValidationError(
                'This field may not be blank',
                code='authorization'
            )
        elif Staff.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError(
                'Entered Email already registered',
                code='authorization'
            )
        return value
    
    def create(self, validated_data: Dict[str, Any]):
        user = Staff.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, data: Dict[str, Any]):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise serializers.ValidationError('Both email and password are required.')

        return data

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
