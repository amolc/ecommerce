from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Staff
from .serializers import StaffSerializer

# List and Create View for Staff
class StaffListView(APIView):
    def get(self, request):
        """Retrieve all staff records."""
        staff = Staff.objects.all()
        serializer = StaffSerializer(staff, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Create a new staff member."""
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve, Update, and Delete View for a Single Staff
class StaffDetailView(APIView):
    def get_object(self, pk):
        try:
            return Staff.objects.get(pk=pk)
        except Staff.DoesNotExist:
            return None

    def get(self, request, pk):
        """Retrieve a single staff member by ID."""
        staff = self.get_object(pk)
        if staff is None:
            return Response({"error": "Staff not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StaffSerializer(staff)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """Update an existing staff member."""
        staff = self.get_object(pk)
        if staff is None:
            return Response({"error": "Staff not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StaffSerializer(staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete a staff member."""
        staff = self.get_object(pk)
        if staff is None:
            return Response({"error": "Staff not found"}, status=status.HTTP_404_NOT_FOUND)
        staff.delete()
        return Response({"message": "Staff deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
