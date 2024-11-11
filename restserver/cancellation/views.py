from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cancellation
from .serializers import CancellationSerializer
from django.shortcuts import get_object_or_404

class CancellationViews(APIView):
    
    def post(self, request, org_id=None):
        request_data = request.data.copy()
        request_data['org_id'] = org_id  # Add org_id to the request data

        serializer = CancellationSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None, org_id=None):
        if id:
            cancellation = get_object_or_404(Cancellation, id=id)
            serializer = CancellationSerializer(cancellation)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        cancellations = Cancellation.objects.filter(org_id=org_id)  # Filter by org_id if provided
        serializer = CancellationSerializer(cancellations, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None, org_id=None):
        cancellation = get_object_or_404(Cancellation, id=id)
        serializer = CancellationSerializer(cancellation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, org_id=None):
        cancellation = get_object_or_404(Cancellation, id=id)
        cancellation.delete()
        return Response({"status": "success", "message": "Cancellation deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
