from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Billing
from customers.models import Customers
from .serializers import BillingSerializer
from django.shortcuts import get_object_or_404

class BillingViews(APIView):
    """
    API view to handle Billing operations.
    """

    def post(self, request, org_id=None):
        """
        Create a new billing record, optionally associating with an org_id.
        """
        request_data = request.data.copy()
        request_data['org_id'] = org_id
        request_data['is_paid'] = False  # Assuming a default "unpaid" status
        
        print("Request Data:", request_data)
        serializer = BillingSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        
        # Handle serializer errors
        print("Serializer Errors:", serializer.errors)
        return Response({"status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None,org_id=None):
        """
        Retrieve billing details by ID or list all billings.
        """
        if id:
            billing = get_object_or_404(Billing, id=id)
            serializer = BillingSerializer(billing)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        billings = Billing.objects.all()
        serializer = BillingSerializer(billings, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None, org_id=None):
        """
        Partially update a billing record by ID and optionally validate org_id.
        """
        if not id:
            return Response(
                {"status": "error", "message": "Billing ID is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        billing = get_object_or_404(Billing, id=id)

        # Validate org_id if provided
        if org_id and billing.org_id != org_id:
            return Response(
                {"status": "error", "message": "Billing record does not match the provided org_id."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = BillingSerializer(billing, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response({"status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, org_id=None):
        """
        Delete a billing record by ID.
        """
        if not id:
            return Response(
                {"status": "error", "message": "Billing ID is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        billing = get_object_or_404(Billing, id=id)
        billing.delete()
        return Response(
            {"status": "success", "message": "Billing deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )
