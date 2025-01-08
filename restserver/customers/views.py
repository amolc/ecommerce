from rest_framework.views import (  # type: ignore
    APIView
)
from rest_framework.response import (  # type: ignore
    Response
)
from rest_framework import (  # type: ignore
    status
)

from knox.models import AuthToken  # type: ignore

from common.utils import StayVillasResponse

from .serializers import (
    RegisterCustomerSerializer,
    LoginSerializer,
    CustomerSerializer
)

from .models import Customers


class RegisterCustomerViews(APIView):
    def post(self, request, org_id=None):
        request_data = request.data.copy()
        request_data["org_id"] = org_id

        # Use the RegisterCustomerSerializer to handle registration
        serializer_class = RegisterCustomerSerializer(data=request_data)

        if serializer_class.is_valid():
            customer = serializer_class.save()
            response_data = serializer_class.data
            response_data['user_id'] = customer.id

            api_response = Response(
                {
                    "status": "success",
                    "data": response_data,
                },
                status=status.HTTP_201_CREATED
            )
        else:
            api_response = Response(
                {
                    "status": "error",
                    "message": serializer_class.errors,
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        return api_response


class AuthenticateUser(APIView):
    def post(self, request, *args, **kwargs):
        try:
            serializer = LoginSerializer(
                data=request.data,
                context={
                    'request': request
                }
            )
            if serializer.is_valid():
                user_data = Customers.objects.filter(
                    email=request.data['email']
                ).first()

                if not user_data:
                    return Response(
                        {
                            'status': 'error',
                            'message': 'User not found'
                        },
                        status=status.HTTP_404_NOT_FOUND
                    )
                print("Verified User Data:", user_data)
                print("Verified User Data Type:", type(user_data))

                # Confirm the user instance is of the correct model
                if not isinstance(user_data, Customers):
                    return Response(
                        {
                            'status': 'error',
                            'message': 'Invalid user instance.'
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

                token_instance, token = AuthToken.objects.create(
                    user=user_data
                )
                print("Generated Token:", token)

                user_id = user_data.id  # This is the customer_id
                # Optional: Update last login if needed (uncomment if required)
                # Customers.objects.filter(id=user_id).update(lastLogin=datetime.now(timezone.utc))

                is_super_admin = user_data.is_super_admin
                is_admin = user_data.is_admin
                is_customer = user_data.is_customer
                displayName = user_data.first_name
                email_id = user_data.email

                # Prepare the response data
                data = {
                    "status": status.HTTP_200_OK,
                    'user_id': user_id,  # Return user_id (customer_id)
                    'is_super_admin': is_super_admin,
                    'is_admin': is_admin,
                    'is_customer': is_customer,
                    'displayName': displayName,
                    'emailId': email_id,
                    "message": "Logged-in Successfully",
                    "Token": token
                }

                return Response({'status': "success", 'data': data})

            else:
                return Response(
                    {
                        "status": "error",
                        "message": serializer.errors
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

        except Exception as e:
            return StayVillasResponse.exception_error(
                self.__class__.__name__,
                request,
                e
            )


class CustomerViews(APIView):
    def get(self, request, id=None, org_id=None):
        try:
            if id:
                item = Customers.objects.get(id=id)
                serializer = (item)
                return Response(
                    {"status": "success", "data": serializer.data},
                    status=status.HTTP_200_OK,
                )

            items = Customers.objects.all()
            serializer = CustomerSerializer(items, many=True)
            
            return Response(
                {
                    "status": "success",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return StayVillasResponse.exception_error(
                self.__class__.__name__,
                request,
                e
            )

    # Update a customer
    def patch(self, request, id=None, org_id=None):
        request_data = request.data
        request_data["org_id"] = org_id

        if not id:
            return Response(
                {
                    'status': 'error',
                    'message': 'ID is required for update.'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        item = Customers.objects.get(id=id)
        serializer = CustomerSerializer(
            item,
            data=request.data,
            partial=True
        )

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
        request_data = request.data
        request_data["org_id"] = org_id
        if not id:
            return Response(
                {
                    'status': 'error',
                    'message': 'ID is required for deletion'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        item = Customers.objects.get(id=id)
        item.delete()

        return Response(
            {
                'status': 'success',
                'message': 'Customer deleted successfully'
            },
            status=status.HTTP_204_NO_CONTENT
        )
