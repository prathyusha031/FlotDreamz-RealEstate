from django.core.management.base import BaseCommand
from realestate.models import Property, Agent, Blog, Deal


class Command(BaseCommand):
    help = "Seed sample data"

    def handle(self, *args, **kwargs):

        if Property.objects.count() == 0:
            Property.objects.create(
                title="Luxury Villa at Jubilee Hills",
                location="Jubilee Hills, Hyderabad",
                price=8500000,
                description="Luxury 4BHK villa with private garden and modern amenities.",
                property_type="Luxury",
                image="property_images/Luxury_Villa.png"
            )

            Property.objects.create(
                title="Premium 2BHK Apartment",
                location="MVP Colony, Visakhapatnam",
                price=3200000,
                description="Premium apartment in a prime residential area.",
                property_type="Buy",
                image="property_images/2BHK_.jpeg"
            )

            Property.objects.create(
                title="Commercial Office Space",
                location="Vijayawada",
                price=12000000,
                description="Commercial office space in a business district.",
                property_type="Commercial",
                image="property_images/Office_.jpeg"
            )

        if Agent.objects.count() == 0:
            Agent.objects.create(
                name="Ravi Kumar",
                contact="+91 9876543210",
                photo="agent_photos/ravi.jpg"
            )

            Agent.objects.create(
                name="Priya Sharma",
                contact="+91 9123456789",
                photo="agent_photos/priya.jpg"
            )

            Agent.objects.create(
                name="Arjun Reddy",
                contact="+91 9988776655",
                photo="agent_photos/arjun.jpg"
            )

        if Blog.objects.count() == 0:
            Blog.objects.create(
                title="Top Real Estate Investment Trends in 2026",
                author="FlotDreamz Team",
                content="Insights into emerging real estate investment opportunities."
            )

            Blog.objects.create(
                title="5 Key Factors to Consider Before Buying a Property",
                author="FlotDreamz Team",
                content="Important factors every buyer should evaluate."
            )

        if Deal.objects.count() == 0:
            Deal.objects.create(
                title="Summer Property Offer",
                description="Get 10% discount on selected properties.",
                discount_percent=10,
                valid_until="2026-08-31"
            )

        self.stdout.write(self.style.SUCCESS("Sample data added"))