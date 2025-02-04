from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review

class Command(BaseCommand):
    help = "Seed the database with sample data"

    def handle(self, *args, **kwargs):
        # Clear existing data
        Listing.objects.all().delete()
        Booking.objects.all().delete()
        Review.objects.all().delete()

        # Create sample listings
        listings = [
            Listing(title="Cozy Cottage", description="A cozy cottage in the countryside", price_per_night=100.00, location="Countryside", available=True),
            Listing(title="Modern Apartment", description="A stylish apartment in the city", price_per_night=150.00, location="City Center", available=True),
            Listing(title="Beach House", description="A beautiful house by the beach", price_per_night=200.00, location="Beachside", available=False),
        ]

        # Save listings to the database
        for listing in listings:
            listing.save()

        # Create sample bookings
        Booking.objects.create(listing=listings[0], user_name="John Doe", check_in_date="2024-01-01", check_out_date="2024-01-05")
        Booking.objects.create(listing=listings[1], user_name="Jane Smith", check_in_date="2024-02-10", check_out_date="2024-02-15")

        # Create sample reviews
        Review.objects.create(listing=listings[0], user_name="Alice", rating=5, comment="Lovely stay!")
        Review.objects.create(listing=listings[1], user_name="Bob", rating=4, comment="Great apartment, will visit again.")

        self.stdout.write(self.style.SUCCESS("Database seeded successfully"))
