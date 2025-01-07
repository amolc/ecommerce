from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.shortcuts import render
import traceback

# DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from knox.models import AuthToken # type: ignore

# Custom
from .serializers import RegisterAdminSerializer, LoginSerializer, AdminSerializer
from .models import Admin
from common.utils import StayVillasResponse


class RegisterAdminViews(APIView):
    def post(self, request, org_id=None):
        print("Registering Agent", request.data)

        request_data = request.data.copy()
        request_data["org_id"] = org_id

        serializer_class = RegisterAdminSerializer(data=request_data)

        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminViews(APIView):

    def get(self, request, id=None, org_id=None):
        try:
            if id:
                agent = Admin.objects.get(id=id)
                serializer = AdminSerializer(agent)
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

            agents = Admin.objects.all()
            serializer = AdminSerializer(agents, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return StayVillasResponse.exception_error(self.__class__.__name__, request, e)

    def patch(self, request, id=None, org_id=None):
        request_data = request.data
        request_data["org_id"] = org_id

        if not id:
            return Response({'status': 'error', 'message': 'ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)

        agent = Admin.objects.get(id=id)
        serializer = AdminSerializer(agent, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, org_id=None):
        if not id:
            return Response({'status': 'error', 'message': 'ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)

        agent = Admin.objects.get(id=id)
        agent.delete()
        return Response({'status': 'success', 'message': 'Agent deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class LoginViews(APIView):
    def post(self, request, id=None, org_id=None):
        # Pass the request data to the serializer
        serializer = LoginSerializer(data=request.data)

        # Check if the data is valid
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            # Retrieve the user based on the provided email
            user = Admin.objects.filter(email=email).first()

            # Check if user exists and password matches
            if user and user.check_password(password):
                # Directly return a successful login message with user ID
                return Response({
                    'status': 'success',
                    'message': f'Login successful for {email}',
                    'email': email,
                    'agent_id': user.id,
                    # Note: Typically you wouldn't return the password
                }, status=status.HTTP_200_OK)

            # User not found or password incorrect
            return Response({
                'status': 'error',
                'message': 'Invalid email or password'
            }, status=status.HTTP_400_BAD_REQUEST)

        # If the data is not valid, log the errors for debugging
        print("Serializer errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AgentFilterViews(APIView):

    def get(self, request, id=None, org_id=None):
        try:
            if id:
                agent = Admin.objects.get(id=id)
                serializer = AdminSerializer(agent)
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

            agents = Admin.objects.all()
            serializer = AdminSerializer(agents, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return StayVillasResponse.exception_error(self.__class__.__name__, request, e)
