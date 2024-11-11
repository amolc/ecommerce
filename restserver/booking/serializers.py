from rest_framework import serializers
from .models import Booking, EventBooking, Customer

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'age']

class BookingSerializer(serializers.ModelSerializer):
    customers = GuestSerializer(many=True)

    class Meta:
        model = Booking
        fields = '__all__'

    def create(self, validated_data):
        # Extract customer data from validated_data
        customers_data = validated_data.pop('customers')
        # Create the Booking instance
        booking = Booking.objects.create(**validated_data)
        # Create Customer instances
        for customer_data in customers_data:
            customer, created = Customer.objects.get_or_create(**customer_data)
            booking.customers.add(customer)  # Associate customer with booking
        return booking

class EventBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventBooking
        fields = '__all__'
