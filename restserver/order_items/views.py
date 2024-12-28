from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import OrderItems
from .serializers import OrderItemSerializer

# Create your views here.
class Order_ItemView(APIView):
    def get(self, request, org_id=None, id=None):
        if id:
            try:
                print(f"Fetching Order with id: {id}")  # Debugging line
                orderItem = OrderItems.objects.get(id=id)
                serializer = OrderItemSerializer(orderItem)
                print(f"orderItem found: {serializer.data}")  # Debugging line
                return Response(serializer.data, status=status.HTTP_200_OK)
            except OrderItems.DoesNotExist:
                print(f"orderItem with id {id} not found")  # Debugging line
                return Response({"error": "orderItem not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            orderitems = OrderItems.objects.all()  # Fetch all order items
            serializer = OrderItemSerializer(orderitems, many=True)
            print(f"Serialized orderItems: {serializer.data}")  # Debugging line
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, org_id=None):
        """Create a new orderItem."""
        print("Request data:", request.data)  # Print the full request body
        
        try:
            # Create a new orderItem using the request data
            serializer = OrderItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                # Return the success response with the created orderItem
                return Response({
                    "status": "success",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, id=None, org_id=None):
        """Update an existing orderItem by ID."""
        if not id:
            return Response({'status': 'error', 'message': 'ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)

        filter_kwargs = {'id': id}
        if org_id is not None:
            filter_kwargs['org_id'] = org_id

        # Fetch the OrderItems instance
        order_item = get_object_or_404(OrderItems, **filter_kwargs)

        serializer = OrderItemSerializer(order_item, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response({"status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, org_id=None):
        """Delete an existing order by ID."""
        if not id:
            return Response({'status': 'error', 'message': 'ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)
        
        order_item = get_object_or_404(OrderItems, id=id)
        order_item.delete()
        return Response({"status": "success", "message": "Order deleted successfully"}, status=status.HTTP_200_OK)
