from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Products
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from customers.models import Customers  # Ensure Customers is imported


class ProductViews(APIView):
    # POST method to create a product
    def post(self, request, org_id=None):
        print("Request data:", request.data)  # Print the full request body
        
        try:
            # Create a new product using the request data
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                # Return the success response along with the created product
                return Response({
                    "status": "success",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self, request, id=None, category_id=None, org_id=None):
        # If an ID is provided, fetch and return a specific product by ID
        if id:
            product = get_object_or_404(Product, id=id)
            serializer = ProductSerializer(product)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        # Otherwise, fetch products with optional filters
        products = Product.objects.all()

        # Apply category_id filter if provided
        if category_id is not None:
            products = products.filter(category_id=category_id)
        
        # Apply org_id filter if provided
        
        
        # Check if any products matched the filters
        if not products.exists():
            return Response(
                {"status": "success", "data": [], "message": "No products found for the given filters"},
                status=status.HTTP_200_OK
            )

        # Serialize and return the list of filtered products
        serializer = ProductSerializer(products, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    # PATCH method to update a product
    # def patch(self, request, id=None, org_id= None):
    #     if not id:
    #         return Response({'status': 'error', 'message': 'ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)

    #     product = get_object_or_404(Product, id=id)
    #     serializer = ProductSerializer(product, data=request.data, partial=True)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, org_id=None, id=None):
        if not id:
            return Response({'status': 'error', 'message': 'ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)

        # Attempt to fetch the product with both id and org_id
        product = Product.objects.filter(id=id).first()
        if not product:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE method to delete a product
    def delete(self, request,org_id, id):
        try:
            product = Product.objects.get(id=id)
            product.delete()
            return Response({"message": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
