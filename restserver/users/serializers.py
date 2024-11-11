from rest_framework import serializers
from .models import Users

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'password', 'first_name', 'last_name', 'mobile_number', 'city']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Users.objects.create_user(**validated_data)
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'email', 'first_name', 'last_name', 'city', 'mobile_number', 'is_active', 'is_staff']

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )

    def validate(self, data):
        user = Users.objects.filter(email=data.get('email')).first()
        if user and user.check_password(data.get('password')):
            return {'user': user}
        raise serializers.ValidationError('Incorrect credentials')
