from rest_framework import viewsets
from .models import Listing, Booking, Payment, TransactionStatus
from .serializers import ListingSerializer, BookingSerializer
from django.views import View
from django.http import JsonResponse
from django.conf import settings
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import uuid

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

@method_decorator(csrf_exempt, name='dispatch')
class initiatePaymentView(View):
    def post(self, request):
        url = "https://api.chapa.co/v1/transaction/initialize"
        data = json.loads(request.body)
        email = data.get("email")
        amount = data.get("amount")
        phone_number = data.get("phone_number")
        if not email or not amount or not phone_number:
            return JsonResponse({"error": "email, amount and phone_number are required"}, status=400)

        payload = {
            "amount": amount,
            "phone_number": phone_number,
            "currency": "USD",
        }

        headers = {
            "Authorization": f"Bearer {settings.CHAPA_PRIVATE}",
            "Content-Type": "application/json",
        }

        try:
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            if response.status_code == 200:
                data = response.json()
                print(data)
                checkout_url = data.get("data").get("checkout_url")
                transaction_reference = uuid.uuid4().hex
                listing = Listing.objects.get(id=1)
                Payment.objects.create(
                    transaction_reference=transaction_reference,
                    phone_number=phone_number,
                    amount=amount,
                    status=TransactionStatus.PENDING,
                    listing=listing,
                    user_name=email
                )
                return JsonResponse({"checkout_url": checkout_url, "payment_reference": transaction_reference}, status=200)
            else:
                return JsonResponse({"error": "Payment Gateway Error"}, status=response.status_code)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class PaymentStatusView(View):
    def post(self, request):
        base_url = "https://api.chapa.co/v1/transaction/verify/"
        data = json.loads(request.body)
        transaction_reference = data.get("tx_ref")
        payment_reference = data.get("py_ref")


        if not transaction_reference:
            return JsonResponse({"error": "tx_ref is required"}, status=400)

        url = f"{base_url}{transaction_reference}"
        headers = {
            "Authorization": f"Bearer {settings.CHAPA_PRIVATE}",
        }
        response = requests.get(url, headers=headers)
        print(response.json())
        if response.status_code == 200:
            data = response.json()
            status = data.get("data").get("status")
            if status == "success":
                payment = Payment.objects.get(transaction_reference=payment_reference)
                payment.status = TransactionStatus.SUCCESS
                payment.save()
                return JsonResponse({"message": "Payment status updated successfully"}, status=200)
            else:
                payment.status = TransactionStatus.FAILED
                payment.save()
                return JsonResponse({"error": "Payment failed"}, status=400)
        else:
            return JsonResponse({"error": "Payment Gateway Error"}, status=response.status_code)

