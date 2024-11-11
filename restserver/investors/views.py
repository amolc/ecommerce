from django.shortcuts import render
import traceback

# drf
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from knox.models import AuthToken  # type: ignore 

# custom
from .serializers import RegisterInvestorSerializer, LoginSerializer, InvestorSerializer
from .models import Investors
from common.utils import StayVillasResponse


class RegisterInvestorViews(APIView):
    
    def post(self, request, org_id=None):
        request_data = request.data.copy()
        request_data["org_id"] = org_id
        
        serializer = InvestorSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class AuthenticateInvestor(APIView):
    
    def post(self, request, *args, **kwargs):
        try:
            serializer = LoginSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                user = serializer.validated_data['user']
                print("User Instance:", user)
                print("User Instance Type:", type(user))

                # Verify user exists and is an instance of Investors
                user_data = Investors.objects.filter(email=request.data['email']).first()
                if not user_data:
                    return Response({'status': 'error', 'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
                print("Verified User Data:", user_data)
                print("Verified User Data Type:", type(user_data))

                # Confirm the user instance is of the correct model
                if not isinstance(user_data, Investors):
                    return Response({'status': 'error', 'message': 'Invalid user instance'}, status=status.HTTP_400_BAD_REQUEST)

                # Create the token
                token_instance, token = AuthToken.objects.create(user=user_data)
                print("Generated Token:", token)

                user_id = user_data.id
                # Investors.objects.filter(id=user_id).update(lastLogin=datetime.now(timezone.utc))

                is_super_admin = user_data.is_super_admin
                is_admin = user_data.is_admin
                is_investor = user_data.is_investor
                displayName = user_data.first_name
                email_id = user_data.email

                # if profileImage:
                #     profileImage = request.build_absolute_uri(user_data.profileImage.url)
                # else:
                #     profileImage = ''

                data = {
                    "status": status.HTTP_200_OK,
                    'user_id': user_id,
                    'is_super_admin': is_super_admin,
                    'is_admin': is_admin,
                    'is_investor': is_investor,
                    'displayName': displayName,
                    'emailId': email_id,
                    # 'profileImage': profileImage,
                    "message": "Logged-in Successfully",
                    "Token": token
                }

                return Response({'status': "success", 'data': data})

            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return StayVillasResponse.exception_error(self.__class__.__name__, request, e)


class InvestorViews(APIView):

    def get(self, request, id=None, org_id=None):
        try:
            if id:
                item = Investors.objects.get(id=id)
                serializer = InvestorSerializer(item)
                return Response(
                    {"status": "success", "data": serializer.data},
                    status=status.HTTP_200_OK,
                )

            items = Investors.objects.all()
            serializer = InvestorSerializer(items, many=True)
            return Response(
                {"status": "success", "data": serializer.data}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return StayVillasResponse.exception_error(self.__class__.__name__, request, e)
        
    def patch(self, request, id=None, org_id=None):
        request_data = request.data
        request_data["org_id"] = org_id

        print("line 123", request_data)
        if not id:
            return Response({'status': 'error', 'message': 'ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)

        item = Investors.objects.get(id=id)
        print("line 129", item)
        serializer = InvestorSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, org_id=None):
        request_data = request.data
        request_data["org_id"] = org_id
        if not id:
            return Response({'status': 'error', 'message': 'ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)
        
        item = Investors.objects.get(id=id)
        print("line 151", id)
        print("line 151", item)
        item.delete()
        print("line 153", item)
        return Response({'status': 'success', 'message': 'Investor deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
