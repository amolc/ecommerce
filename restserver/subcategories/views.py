from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Subcategory, Category
from .serializers import SubcategorySerializer


class SubcategoryViews(APIView):
    
    # POST method to create a subcategory (using org_id and category_id)
    def post(self, request, org_id):
        # Ensure category_id is provided in the request body
        category_id = request.data.get('category_id')  # Extract category_id from request body

        if not category_id:
            return Response({"status": "error", "message": "Category ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Ensure the category exists in the database
        category = get_object_or_404(Category, id=category_id)

        # Prepare the data for subcategory creation, including org_id and category
        request_data = request.data.copy()
        request_data['category'] = category.id  # Set category field using category_id
        request_data['org_id'] = org_id  # Include org_id in the request data if required

        # Serialize and save the subcategory data
        serializer = SubcategorySerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET method to fetch subcategories by id or filter by category_id
    def get(self, request, id=None, org_id=None, category_id=None):
        subcategories = Subcategory.objects.all()  # Default query

        if category_id:
            subcategories = subcategories.filter(category_id=category_id)

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
