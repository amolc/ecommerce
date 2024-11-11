# django
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from knox.models import AuthToken # type: ignore
from .serializers import RegisterUserSerializer, UserSerializer, LoginSerializer
from .models import Users
import traceback

class RegisterUserView(APIView):
    def post(self, request):
        try:
            serializer = RegisterUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            traceback.print_exc()  # Log the traceback for debugging
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class AuthenticateUser(APIView):
#     def post(self, request):
#         try:
#             serializer = LoginSerializer(data=request.data)
#             if serializer.is_valid():
#                 user = serializer.validated_data['user']
                
#                 # Verify user instance is of the correct model
#                 if not isinstance(user, Users):
#                     return Response({'status': 'error', 'message': 'Invalid user instance'}, status=status.HTTP_400_BAD_REQUEST)
                
#                 # Create the token
#                 token_instance, token = AuthToken.objects.create(user)
                
#                 return Response({
#                     'token': token,
#                     'user': UserSerializer(user).data
#                 })
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             traceback.print_exc()  # Log the traceback for debugging
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserView(APIView):
    def get(self, request, id=None):
        try:
            if id:
                user = Users.objects.get(id=id)
                serializer = UserSerializer(user)
                return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
            users = Users.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        except Users.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            user = Users.objects.get(id=id)
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Users.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            user = Users.objects.get(id=id)
            user.delete()
            return Response({'status': 'success', 'message': 'User deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Users.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
