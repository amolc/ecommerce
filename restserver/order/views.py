from django.shortcuts import render
from rest_framework.views import APIView



# Create your views here.
class OrderViews(APIView):
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

def get(self, request, id=None, org_id=None):
        """Fetch all orders or a specific order by ID."""
        if id:
            # Fetch a specific order by ID
            order = get_object_or_404(Order, id=id)
            serializer = OrderSerializer(order)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        # Fetch all orders if no ID is provided
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

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
