from rest_framework.views import APIView  # type: ignore
from rest_framework.decorators import api_view  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework.request import Request  # type: ignore
from rest_framework import status  # type: ignore

from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

from orders.utils import (
    send_order_confirmation_email
)

from customers.models import (
    Customer
)

from staff.models import (
    Staff
)

from .models import (
    Order,
    OrderItem
)
from .serializers import (
    OrderSerializer,
    OrderItemSerializer
)
from orders.tasks import send_mail
from datetime import datetime

@api_view(['POST'])
def change_order_status(
    request: Request,
    org_id: int | None,
    order_id: int | None
):
    order_status = request.data.get('status')  # type: ignore

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
            original_order_status = order.status
            
            order.status = order_status
            order.save()
            
            # ADD LOGIC TO SEND EMAIL HERE.
            email = order.email
            subject = "Order Status Update"
            full_name = f"{order.customer.first_name} {order.customer.last_name}"  # type: ignore

            body = f"""
            <html>
            <head>
                <style>
                    .header {{
                        font-size: 24px;
                        font-weight: bold;
                        color: green;
                    }}
                    .order-details, .order-items {{
                        margin-top: 20px;
                    }}
                    .order-items th, .order-items td {{
                        border: 1px solid #ddd;
                        padding: 8px;
                    }}
                    .order-items th {{
                        background-color: #f2f2f2;
                    }}
                    .order-summary {{
                        margin-top: 20px;
                        font-weight: bold;
                    }}
                </style>
            </head>
            <body>
                <p class="header">Order Status Update</p>
                <p>Dear { full_name },</p>
                <p>Your order status has been updated from <strong>{original_order_status}</strong> to <strong>{order_status}</strong>.</p>
                <div class="order-details">
                    <p><strong>Order Details:</strong></p>
                    <p>Order ID: {order.id}</p>
                    <p>Order Date: {order.created_at.strftime('%Y-%m-%d')}</p>
                </div>
                <div class="order-items">
                    <p><strong>Items:</strong></p>
                    <table>
                        <tr>
                            <th>Product Name</th>
                            <th>Quantity</th>
                            <th>Price</th>
                        </tr>
            """
            
            for item in order.order_items.all():  # type: ignore
                body += f"""
                        <tr>
                            <td>{item.product_name}</td>
                            <td>{item.product_qty}</td>
                            <td>₹{item.product_price}</td>
                        </tr>
                """
            body += f"""
                    </table>
                </div>
                <div class="order-summary">
                    <p>Total Amount: ₹{order.amount}</p>
                </div>
                <p>Thank you for shopping with us.</p>
                <p>Best regards,</p>
                <p>Pamosapicks</p>
            </body>
            </html>
            """
            send_mail(email, subject, body)

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
        except ValidationError as e:
            return Response(
                {
                    "status": "error",
                    "message": e.message
                }
            )

@api_view(['POST'])
def change_order_assigned_to(
    request: Request,
    org_id: int | None,
    order_id: int | None
):
    assigned_to_id = request.data.get('assigned_to')  # type: ignore

    if not assigned_to_id:
        return Response(
            {"status": "error", "message": "Assigned staff member not submitted."},
            status=status.HTTP_400_BAD_REQUEST
        )
    else:
        try:
            order = Order.objects.get(id=order_id)
            staff_member = Staff.objects.get(id=assigned_to_id)
            order.assigned_to = staff_member
            order.save()

            serializer = OrderSerializer(order)

            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        except Order.DoesNotExist:
            return Response(
                {"status": "error", "message": "Order not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Staff.DoesNotExist:
            return Response(
                {"status": "error", "message": "Staff member not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        except ValidationError as e:
            return Response(
                {"status": "error", "message": e.message}
            )

@api_view(['POST'])
def change_order_delivery_date(
    request: Request,
    org_id: int | None,
    order_id: int | None
):
    delivery_date = request.data.get('delivery_date')  # type: ignore
    try:
        delivery_date = datetime.strptime(delivery_date, '%Y-%m-%dT%H:%M:%S.%fZ').date()
    except ValueError:
        return Response(
            {"status": "error", "message": "Invalid delivery date format."},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if not delivery_date:
        return Response(
            {"status": "error", "message": "Delivery date not submitted."},
            status=status.HTTP_400_BAD_REQUEST
        )
    try:
        order = Order.objects.get(id=order_id)
        order.delivery_date = delivery_date
        order.save()
        serializer = OrderSerializer(order)
        return Response(
            {"status": "success", "data": serializer.data},
            status=status.HTTP_200_OK
        )
    except Order.DoesNotExist:
        return Response(
            {"status": "error", "message": "Order not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    except ValidationError as e:
        return Response(
            {"status": "error", "message": e.message}
        )

class OrderViews(APIView):
    def get(
        self,
        request: Request,
        org_id: int | None=None,
        order_id: int | None=None
    ):
        customer_id = request.query_params.get('customer_id')
        status_param = request.query_params.get('status')

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
            if status_param:
                orders = orders.filter(status=status_param)
            serializer = OrderSerializer(orders, many=True)
            return Response(
                {
                    "status": "success",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )

    def post(
        self,
        request: Request,
        org_id: int | None=None
    ):
        order_data = request.data
        print(order_data)
        
        try:
           
            serializer = OrderSerializer(data=order_data)
            if serializer.is_valid():
                serializer.save()

                order_id = serializer.data['id']
                # Let's send an email to the customer
                customer_email = serializer.validated_data['customer'].email
                customer_name = serializer.validated_data['customer'].first_name + serializer.validated_data['customer'].last_name
                order_status = serializer.data['status']                
                order_items = serializer.data['order_items']  

                send_order_confirmation_email(customer_email, customer_name, order_id, order_status, order_items)
                # send_telegram_message(customer_email, customer_name, order_id, order_status, order_items)

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

    def patch(
        self,
        request: Request,
        id: int | None=None,
        org_id: int | None=None
    ):
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

    def delete(
        self,
        request: Request,
        id: int | None=None, org_id: int | None=None):
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
    def get(
        self,
        request: Request,
        org_id: int | None=None,
        id: int | None=None
    ):
        if id:
            try:
                order_item = OrderItem.objects.get(id=id)
                serializer = OrderItemSerializer(
                    order_item
                )
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )
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

    def post(self, request: Request, org_id: int | None=None):
        """Create a new orderItem."""
        print("Request data:", request.data)

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

    def patch(
        self,
        request: Request,
        id: int | None=None,
        org_id: int | None=None
    ):
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

    def delete(
        self,
        request: Request,
        id: int | None=None,
        org_id: int | None=None
    ):
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
