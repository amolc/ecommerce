from rest_framework import serializers
from .models import Billing
from customers.models import Customers  # Import the Customers model

class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for the Customer model to include customer details."""
    class Meta:
        model = Customers
        fields = ['id', 'first_name', 'last_name', 'email', 'city', 'mobile_number']  # Include customer-specific fields

class BillingSerializer(serializers.ModelSerializer):
    """Serializer for the Billing model to include billing details along with customer details."""
    customer = CustomerSerializer()  # Nesting the Customer serializer within the Billing serializer

    class Meta:
        model = Billing
        fields = [
            'id', 'first_name', 'last_name', 'email', 'city', 'mobile_number', 'customer',  # Customer-related fields
            'org_id', 'billing_address', 'city', 'state', 'postal_code', 'country',  # Billing-related fields
            'billing_date', 'total_amount', 'is_paid'
        ]
    
    def create(self, validated_data):
        """Custom create method to handle nested customer data."""
        customer_data = validated_data.pop('customer')  # Extract customer data from the validated data
        # You can either create a new customer or assume the customer already exists and link it to the billing
        customer, created = Customers.objects.get_or_create(**customer_data)  # Assuming a customer is created or fetched
        billing = Billing.objects.create(customer=customer, **validated_data)  # Create the billing record and associate it with the customer
        return billing

    def update(self, instance, validated_data):
        """
        Custom update method to handle nested customer data.
        """
        customer_data = validated_data.pop('customer', None)  # Extract nested customer data if present

        # Update customer details if provided
        if customer_data:
            customer = instance.customer
            for key, value in customer_data.items():
                setattr(customer, key, value)  # Update customer fields
            customer.save()  # Save updated customer data

        # Update billing details
        for key, value in validated_data.items():
            setattr(instance, key, value)  # Update billing fields
        instance.save()  # Save updated billing data

        return instance
