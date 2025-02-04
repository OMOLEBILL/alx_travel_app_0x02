from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'price_per_night', 'location', 'available']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'listing', 'user_name', 'check_in_date', 'check_out_date']
