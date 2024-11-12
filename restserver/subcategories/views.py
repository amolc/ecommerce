from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Subcategory
from .serializers import SubcategorySerializer

class SubcategoryViews(APIView):
    
    # POST method to create a subcategory (using org_id and category_id)
    def post(self, request, org_id, category_id=None,):
        # Optionally add category_id to request data if needed for subcategory creation
        request_data = request.data.copy()
        request_data['category_id'] = category_id  # Assuming category_id is part of the subcategory data
        request_data['org_id'] = org_id  # Include org_id in the request data if required

        serializer = SubcategorySerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET method to fetch subcategories by id or filter by category_id
    def get(self, request, id=None, org_id=None, category_id=None):
        if id:
            # Fetch a specific subcategory by ID
            subcategory = get_object_or_404(Subcategory, id=id)
            serializer = SubcategorySerializer(subcategory)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        # If org_id is passed, filter subcategories based on org_id and category_id
        subcategories = Subcategory.objects.all()  # Default query

        if org_id:
            subcategories = subcategories.filter(org_id=org_id)
        if category_id:
            subcategories = subcategories.filter(category_id=category_id)

        # Serialize and return all subcategories
        serializer = SubcategorySerializer(subcategories, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    # PATCH method to update a subcategory
    def patch(self, request, id=None, org_id=None, category_id=None):
        if not id:
            return Response({'status': 'error', 'message': 'ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)

        subcategory = get_object_or_404(Subcategory, id=id)
        serializer = SubcategorySerializer(subcategory, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE method to delete a subcategory
    def delete(self, request, id=None, org_id=None, category_id=None):
        if not id:
            return Response({'status': 'error', 'message': 'ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)

        subcategory = get_object_or_404(Subcategory, id=id)
        subcategory.delete()
        return Response({"status": "success", "message": "Subcategory deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
