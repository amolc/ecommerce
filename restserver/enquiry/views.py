from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Enquiry
from .serializers import EnquirySerializer
from django.shortcuts import get_object_or_404

class EnquiryViews(APIView):
    
    def post(self, request, org_id=None):
        request_data = request.data.copy()
        request_data['org_id'] = org_id

        serializer = EnquirySerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None, org_id=None):
        if id:
            enquiry = get_object_or_404(Enquiry, id=id)
            serializer = EnquirySerializer(enquiry)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        enquiries = Enquiry.objects.all()
        serializer = EnquirySerializer(enquiries, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None, org_id=None):
        enquiry = get_object_or_404(Enquiry, id=id)
        serializer = EnquirySerializer(enquiry, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, org_id=None):
        enquiry = get_object_or_404(Enquiry, id=id)
        enquiry.delete()
        return Response({"status": "success", "message": "Enquiry deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
