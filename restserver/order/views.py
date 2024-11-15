from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer
from django.shortcuts import get_object_or_404


# Create your views here.
class OrderViews(APIView):
    def get(self, request, org_id=None, order_id=None):
        if order_id:
            try:
                print(f"Fetching Order with id: {order_id}")  # Debugging line
                order = Order.objects.get(order_id=order_id)
                serializer = OrderSerializer(order)
                print(f"Order found: {serializer.data}")  # Debugging line
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Order.DoesNotExist:
                print(f"Order with id {order_id} not found")  # Debugging line
                return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            orders = Order.objects.all()
            print(f"Fetched orders: {orders}")  # Debugging line
            serializer = OrderSerializer(orders, many=True)
            print(f"Serialized orders: {serializer.data}")  # Debugging line
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, org_id=None):
        """Create a new order."""
        print("Request data:", request.data)  # Print the full request body
        
        try:
            # Create a new order using the request data
            serializer = OrderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                # Return the success response with the created order
                return Response({
                    "status": "success",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def patch(self, request, id=None, org_id=None):
        """Update an existing order by ID."""
        if not id:
            return Response({'status': 'error', 'message': 'ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)

        order = get_object_or_404(Order, id=id)
        serializer = OrderSerializer(order, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(self, request, id=None, org_id=None):
    """Delete an existing order by ID."""
    if not id:
        return Response({'status': 'error', 'message': 'ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)
    
    order = get_object_or_404(Order, id=id)
    order.delete()
    return Response({"status": "success", "message": "Order deleted successfully"}, status=status.HTTP_200_OK)
