from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PropertyListing
from .serializers import PropertyListingSerializer

class PropertyListingViews(APIView):

    # GET - Retrieve one or all property listings
    def get(self, request, id=None, org_id=None):
        try:
            if id:
                item = PropertyListing.objects.get(id=id)
                serializer = PropertyListingSerializer(item)
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

            items = PropertyListing.objects.filter(org_id=org_id)
            serializer = PropertyListingSerializer(items, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # POST - Create a new property listing
    def post(self, request, org_id=None):
        request_data = request.data.copy()
        request_data["org_id"] = org_id
        
        serializer = PropertyListingSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PATCH - Update a specific property listing
    def patch(self, request, id=None, org_id=None):
        request_data = request.data.copy()
        request_data["org_id"] = org_id
        
        if not id:
            return Response({'status': 'error', 'message': 'ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            item = PropertyListing.objects.get(id=id)
            serializer = PropertyListingSerializer(item, data=request_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PropertyListing.DoesNotExist:
            return Response({'status': 'error', 'message': 'Property listing not found'}, status=status.HTTP_404_NOT_FOUND)

    # DELETE - Delete a property listing
    def delete(self, request, id=None, org_id=None):
        if not id:
            return Response({'status': 'error', 'message': 'ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            item = PropertyListing.objects.get(id=id)
            item.delete()
            return Response({'status': 'success', 'message': 'Property listing deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except PropertyListing.DoesNotExist:
            return Response({'status': 'error', 'message': 'Property listing not found'}, status=status.HTTP_404_NOT_FOUND)
