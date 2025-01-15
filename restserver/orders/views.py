from rest_framework.views import APIView  # type: ignore
from rest_framework.decorators import api_view  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status  # type: ignore

from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

from customers.models import (
    Customer
)

from organisations.models import (
    Organisation
)

from .models import (
    Order,
    OrderItem
)
from .serializers import (
    OrderSerializer,
    OrderItemSerializer
)

@api_view(['POST'])
def change_order_status(request, org_id, order_id):
    order_status = request.data.get('status')

    if not order_status:
        return Response(
            {
                "status": "error",
                "message": "Order status not submitted."
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    else:
        try:
            order = Order.objects.get(id=order_id)
            order.status = order_status
            order.save()

            serializer = OrderSerializer(order)

            return Response(
                {
                    "status": "success",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
        except Order.DoesNotExist:
            return Response(
                {
                    "status": "error",
                    "message": "Order not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except ValidationError:
            return Response(
                {
                    "status": "error",
                    "message": (
                        "The status you've attempted to "
                        "set is not supported."
                    )
                }
            )


class OrderViews(APIView):
    def get(self, request, org_id=None, order_id=None):
        customer_id = request.query_params.get('customer_id')

        if order_id:
            try:
                order = Order.objects.get(id=order_id)
                serializer = OrderSerializer(order)
                return Response(
                    {
                        "status": "success",
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK
                )
            except Order.DoesNotExist:
                return Response(
                    {
                        "status": "error",
                        "message": "Order not found"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
        elif customer_id:
            customer = Customer.objects.get(id=customer_id)
            orders = Order.objects.filter(
                customer=customer
            )
            serializer = OrderSerializer(orders, many=True)
            
            return Response(
                {
                    "status": "success",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        else:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response(
                {
                    "status": "success",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )

    def post(self, request, org_id=None):
        order_data = request.data

        try:
            serializer = OrderSerializer(data=order_data)
            if serializer.is_valid():
                serializer.save()

                return Response({
                    "status": "success",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    {
                        "status": "error",
                        "message": str(serializer.errors)
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

        except Exception as e:
            return Response(
                {
                    "status": "error",
                    "message": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def patch(self, request, id=None, org_id=None):
        if not id:
            return Response(
                {
                    'status': 'error',
                    'message': 'ID is required for update'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        order = get_object_or_404(Order, id=id)

        serializer = OrderSerializer(order, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "success",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, org_id=None):
        """Delete an existing order by ID."""
        if not id:
            return Response(
                {
                    'status': 'error',
                    'message': 'ID is required for deletion'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        order = get_object_or_404(Order, id=id)
        order.delete()

        return Response(
            {
                "status": "success",
                "message": "Order deleted successfully"
            },
            status=status.HTTP_200_OK
        )


class OrderItemViews(APIView):
    def get(self, request, org_id=None, id=None):
        if id:
            try:
                order_item = OrderItem.objects.get(id=id)
                serializer = OrderItemSerializer(
                    order_item
                )
                return Response(serializer.data, status=status.HTTP_200_OK)
            except OrderItem.DoesNotExist:
                print(f"orderItem with id {id} not found")  # Debugging line
                return Response(
                    {"error": "orderItem not found"},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            orderitems = OrderItem.objects.all()  # Fetch all order items
            serializer = OrderItemSerializer(orderitems, many=True)
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
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )

        except Exception as e:
            return Response(
                {"status": "error", "message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def patch(self, request, id=None, org_id=None):
        """Update an existing orderItem by ID."""
        if not id:
            return Response(
                {'status': 'error', 'message': 'ID is required for update'},
                status=status.HTTP_400_BAD_REQUEST
            )

        filter_kwargs = {'id': id}
        if org_id is not None:
            filter_kwargs['org_id'] = org_id

        order_item = get_object_or_404(OrderItem, **filter_kwargs)
        serializer = OrderItemSerializer(
            order_item,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK
            )

        return Response(
            {"status": "error", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id=None, org_id=None):
        """Delete an existing order by ID."""
        if not id:
            return Response(
                {'status': 'error', 'message': 'ID is required for deletion'},
                status=status.HTTP_400_BAD_REQUEST
            )

        order_item = get_object_or_404(OrderItem, id=id)
        order_item.delete()
        return Response(
            {"status": "success", "message": "Order deleted successfully"},
            status=status.HTTP_200_OK
        )
