from django.shortcuts import render
from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Listing instances.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Booking instances.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

