from rest_framework.views import APIView  # type: ignore
from rest_framework.decorators import api_view  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status  # type: ignore

from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

from .models import Order
from .serializers import OrderSerializer


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
