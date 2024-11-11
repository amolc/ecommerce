# drf
from django.contrib.auth import authenticate
from rest_framework import serializers

# custom
import re
from .models import Customers

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None

def is_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    match = re.match(pattern, email)
    return match is not None

class RegisterCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError('This field may not be blank', code='authorization')
        elif Customers.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError('Entered Email already registered', code='authorization')
        return value
    
    def create(self, validated_data):
        user = Customers.objects.create_user(**validated_data)
        return user


    


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(
        label=("password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        max_length=125,
        write_only=True
    )

    class Meta:
        model = Customers
        fields =  '__all__'


    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if email and password:
                            
            #authenticate userdetails 
            if is_email(email):
                # authenticate user details
                user = EmailBackend.authenticate(self, request=self.context.get('request'), email=email,
                 password=password)
            
                print("======user===", user)
                if not user:
                    message = {'incorrectuser':'The email you entered does not exists'}
                    raise serializers.ValidationError(message, code='authorization')
                
                if not user.check_password(password):
                    message = {'incorrectpassword':'Entered password was not matching'}
                    raise serializers.ValidationError(message, code='authorization')           


        else:
            message = {'message':'Must include "Username" and "Password"'}
            raise serializers.ValidationError(message, code='authorization')

        data['user'] = data
        return data
    

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'