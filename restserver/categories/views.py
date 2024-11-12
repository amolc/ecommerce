from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer

class CategoryAPIView(APIView):
    # GET method to retrieve all categories or a specific one by id
    def get(self, request, org_id=None, category_id=None):
        if category_id:
            try:
                category = Category.objects.get(id=category_id)
                serializer = CategorySerializer(category)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Category.DoesNotExist:
                return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    # POST method to create a new category
    def post(self, request,org_id, *args, **kwargs):  # Removed org_id as it's not being used
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Assuming no org_id or other additional fields are needed
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT method to update an existing category
    def put(self, request,org_id, category_id):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategorySerializer(category, data=request.data, partial=True)  # Partial updates allowed
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE method to delete a category
    def delete(self, request,org_id, category_id):
        try:
            category = Category.objects.get(id=category_id)
            category.delete()
            return Response({"message": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
