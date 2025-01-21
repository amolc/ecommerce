from rest_framework.request import Request  # type: ignore
from rest_framework.views import APIView  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status  # type: ignore

from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import Inventory
from .serializers import InventorySerializer

from products.models import (
    Product
)


class InventoryViews(APIView):
    def post(self, request: Request, org_id: int | None=None):
        # Ensure you don't require org_id for the product
        product_id = request.data.get('product')  # type: ignore

        try:
            product = Product.objects.get(id=product_id)

            data = request.data
            data['product'] = product.id

            serializer = InventorySerializer(
                data=data,
                context={'org_id': org_id}
            )

            if serializer.is_valid():
                serializer.save()  # Save the inventory
                return Response({
                    "status": "success",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )

        except Product.DoesNotExist:
            return Response(
                {"status": "error", "message": "Product not found."},
                status=status.HTTP_404_NOT_FOUND
            )

    def get(
        self,
        request: Request,
        org_id: int | None=None,
        product_id: int | None=None
    ):
        if product_id:
            inventory = get_object_or_404(Inventory, product_id=product_id)
            serializer = InventorySerializer(inventory)
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK
            )

        inventory = Inventory.objects.all()  # type: ignore

        serializer = InventorySerializer(inventory, many=True)
        return Response(
            {"status": "success", "data": serializer.data},
            status=status.HTTP_200_OK
        )

    def patch(self, request: Request, org_id: int | None=None):
        product_id = request.data.get('product')  # type: ignore
        restock_quantity = request.data.get('restock_quantity')  # type: ignore

        if not restock_quantity:
            return Response({
                "status": "error",
                "message": (
                    "restock_quantity is required "
                    "to increase inventory."
                )
            }, status=status.HTTP_400_BAD_REQUEST)

        # Get the product
        product = get_object_or_404(Product, id=product_id)

        # Check if the product has an associated inventory
        try:
            inventory = product.inventory  # type: ignore
        except Inventory.DoesNotExist:
            return Response({
                "status": "error",
                "message": "Inventory for the product does not exist."
            }, status=status.HTTP_404_NOT_FOUND)

        inventory.stock_quantity += restock_quantity
        inventory.restock_quantity = restock_quantity
        inventory.last_restock_date = timezone.now()

        inventory.save()

        serializer = InventorySerializer(inventory)
        return Response({
            "status": "success",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def delete(
        self,
        request: Request,
        org_id: int | None=None,
        product_id: int | None=None
    ):
        try:
            inventory = get_object_or_404(Inventory, product_id=product_id)
            inventory.delete()
            return Response(
                {"message": "Inventory deleted successfully"},
                status=status.HTTP_204_NO_CONTENT
            )
        except Inventory.DoesNotExist:
            return Response(
                {"error": "Inventory not found"},
                status=status.HTTP_404_NOT_FOUND
            )
