from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404

class ProductViews(APIView):
    # POST method to create a product
    def post(self, request, org_id=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET method to fetch all products or filter by category or org_id
    def get(self, request, id=None, category_id=None, org_id=None):
        if id:
            # Fetch a specific product by ID
            product = get_object_or_404(Product, id=id)
            serializer = ProductSerializer(product)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        # Fetch products by filters if provided
        products = Product.objects.all()

        if category_id:
            products = products.filter(category_id=category_id)
        if org_id:
            products = products.filter(org_id=org_id)

        serializer = ProductSerializer(products, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    # PATCH method to update a product
    def patch(self, request, id=None, org_id= None):
        if not id:
            return Response({'status': 'error', 'message': 'ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)

        product = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(product, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE method to delete a product
    def delete(self, request, id=None, org_id= None):
        if not id:
            return Response({'status': 'error', 'message': 'ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)

        product = get_object_or_404(Product, id=id)
        product.delete()
        return Response({"status": "success", "message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
