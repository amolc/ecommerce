from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PropertyManager
from .serializers import PropertyManagerSerializer
from django.shortcuts import get_object_or_404

class PropertyManagerViews(APIView):
    
    def post(self, request, org_id=None):
        request_data = request.data.copy()
        request_data['org_id'] = org_id
        
        serializer = PropertyManagerSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None, org_id=None):
        if id:
            property_manager = get_object_or_404(PropertyManager, id=id)
            serializer = PropertyManagerSerializer(property_manager)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
        property_managers = PropertyManager.objects.all()
        serializer = PropertyManagerSerializer(property_managers, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None, org_id=None):
        property_manager = get_object_or_404(PropertyManager, id=id)
        serializer = PropertyManagerSerializer(property_manager, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, org_id=None):
        property_manager = get_object_or_404(PropertyManager, id=id)
        property_manager.delete()
        return Response({"status": "success", "message": "Property Manager deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
