from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Inventory
from .serializers import InventorySerializer
from product.models import Products
from django.shortcuts import get_object_or_404
from django.utils import timezone



class InventoryViews(APIView):
    def post(self, request, org_id=None):
        # Ensure you don't require org_id for the product
        product_id = request.data.get('product')
        
        try:
            # Fetch the product without checking for org_id
            product = Products.objects.get(id=product_id)
            
            # Prepare the data and pass to serializer
            data = request.data
            data['product'] = product.id  # Ensure the product is referenced correctly
            
            serializer = InventorySerializer(data=data, context={'org_id': org_id})
            
            if serializer.is_valid():
                serializer.save()  # Save the inventory
                return Response({
                    "status": "success",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Products.DoesNotExist:
            return Response({"status": "error", "message": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

    # GET method to fetch inventory
    def get(self, request, org_id=None, product_id=None):
        if product_id:
            # Fetch inventory for specific product and org_id
            inventory = get_object_or_404(Inventory, product_id=product_id)
            serializer = InventorySerializer(inventory)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        # Fetch all inventories for the given org_id, allowing for org_id being null
        inventory = Inventory.objects.all()
       

        serializer = InventorySerializer(inventory, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    # PATCH method to update inventory
    def patch(self, request, org_id=None):
        # Fetch the inventory for the given product ID
        product_id = request.data.get('product')
        restock_quantity = request.data.get('restock_quantity')

        if not restock_quantity:
            return Response({
                "status": "error",
                "message": "restock_quantity is required to increase inventory."
            }, status=status.HTTP_400_BAD_REQUEST)

        # Get the product
        product = get_object_or_404(Products, id=product_id)
        
        # Check if the product has an associated inventory
        try:
            inventory = product.inventory
        except Inventory.DoesNotExist:
            return Response({
                "status": "error",
                "message": "Inventory for the product does not exist."
            }, status=status.HTTP_404_NOT_FOUND)

        # Increase the stock quantity
        inventory.stock_quantity += restock_quantity
        inventory.restock_quantity = restock_quantity
        inventory.last_restock_date = timezone.now()  # Set the current date and time

        
        # Save the updated inventory
        inventory.save()

        # Serialize and return the updated inventory
        serializer = InventorySerializer(inventory)
        return Response({
            "status": "success",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    # DELETE method to remove inventory for a product
    def delete(self, request, org_id=None, product_id=None):
        try:
            inventory = get_object_or_404(Inventory, product_id=product_id)
            inventory.delete()
            return Response({"message": "Inventory deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Inventory.DoesNotExist:
            return Response({"error": "Inventory not found"}, status=status.HTTP_404_NOT_FOUND)
