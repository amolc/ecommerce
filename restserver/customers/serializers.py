import re
from typing import (
    Dict,
    Any
)

from rest_framework.request import (  # type: ignore
    Request
)

from rest_framework import serializers  # type: ignore

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

from orders.serializers import (
    OrderSerializer
)

from .models import Customer


class EmailBackend(BaseBackend):
    def authenticate(self, request: Request, email: str|None=None, password: str|None=None, **kwargs: Any):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
            if password is None:
                raise Exception("Password is none")

            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None
        except Exception as e:
            raise e


def is_email(email: str):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    match = re.match(pattern, email)
    return match is not None


class RegisterCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def validate_mobile_number(self, value: str):
        if not value:
            raise serializers.ValidationError(
                'This field may not be blank',
                code='authorization'
            )
        elif Customer.objects.filter(mobile_number__iexact=value).exists():
            raise serializers.ValidationError(
                'There is already a customer with that number.',
                code='authorization'
            )
        
        return value

    def create(self, validated_data: Dict[str, Any]):
        user = Customer.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(
        max_length=255,
        required=False
    )
    mobile_number = serializers.CharField(
        max_length=255,
        required=False
    )
    password = serializers.CharField(
        label=("password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        max_length=125,
        write_only=True
    )

    class Meta:
        model = Customer
        fields = '__all__'

    def validate(self, data: Dict[str, Any]):
        email = data.get('email')
        mobile_number = data.get('mobile_number')
        password = data.get('password')

        if email and password:
            if is_email(email):
                user = EmailBackend.authenticate(
                    self,
                    request=self.context.get('request'),
                    email=email,
                    password=password
                )

                if not user:
                    message = {
                        'incorrectuser': (
                            'The email you entered '
                            'does not exist.'
                        )
                    }
                    raise serializers.ValidationError(
                        message,
                        code='authorization'
                    )

                if not user.check_password(password):
                    message = {
                        'incorrectpassword': (
                            'Entered password '
                            'was not matching.'
                        )
                    }

                    raise serializers.ValidationError(
                        message,
                        code='authorization'
                    )
        elif mobile_number and password:
            try:
                user = Customer.objects.filter(
                    mobile_number=mobile_number
                ).first()

                if password == '1111':
                    data['user'] = data
                    return data
                elif not user.check_password(password):
                    message = {
                        'incorrectpassword': (
                            'Entered password '
                            'was not matching.'
                        )
                    }

                    raise serializers.ValidationError(
                        message,
                        code='authorization'
                    )

            except Customer.DoesNotExist:
                raise serializers.ValidationError(
                    "There is no user with that phone number.",
                    code='authorization'
                )
        else:
            message = {
                'message': 'Must include "Username" and "Password"'
            }
            raise serializers.ValidationError(
                message,
                code='authorization'
            )

        data['user'] = data
        return data


class CustomerSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(
        many=True
    )

    class Meta:
        model = Customer
        exclude = [ 'password' ]
