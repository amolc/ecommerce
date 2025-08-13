from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from django.db import transaction
from .models import Category
from .serializers import CategorySerializer
from rest_framework.exceptions import ValidationError  
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.serializers import Serializer
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    """
    A comprehensive ViewSet for Category CRUD operations.
    
    Provides the following endpoints:
    - GET /categories/ - List all categories
    - POST /categories/ - Create a new category
    - GET /categories/{id}/ - Retrieve a specific category
    - PUT /categories/{id}/ - Update a specific category
    - PATCH /categories/{id}/ - Partially update a specific category
    - DELETE /categories/{id}/ - Delete a specific category
    - GET /categories/active/ - List only active categories
    - POST /categories/{id}/toggle_status/ - Toggle category active status
    """
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser, FormParser)
    
    def list(self, request, *args, **kwargs):
        """
        List all categories with optional filtering.
        """
        try:
            # Get query parameters for filtering
            is_active = request.query_params.get('is_active', None)
            organisation_id = request.query_params.get('organisation', None)
            
            queryset = self.get_queryset()
            
            # Apply filters
            if is_active is not None:
                queryset = queryset.filter(is_active=is_active.lower() == 'true')
            
            if organisation_id:
                queryset = queryset.filter(organisation_id=organisation_id)
            
            # Serialize the queryset
            serializer = self.get_serializer(queryset, many=True)
            
            return Response({
                'status': 'success',
                'message': 'Categories retrieved successfully',
                'data': serializer.data,
                'count': queryset.count()
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error retrieving categories: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def create(self, request, *args, **kwargs):
        """
        Create a new category with multipart/form-data support.
        """
        try:
            with transaction.atomic():
                serializer = self.get_serializer(data=request.data)
                
                if serializer.is_valid():
                    category = serializer.save()
                    
                    return Response({
                        'status': 'success',
                        'message': 'Category created successfully',
                        'data': serializer.data
                    }, status=status.HTTP_201_CREATED)
                else:
                    return Response({
                        'status': 'error',
                        'message': 'Invalid data provided',
                        'errors': serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST)
                    
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error creating category: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a specific category by ID.
        """
        category = self.get_object()
        serializer = self.get_serializer(category)
        
        return Response({
            'status': 'success',
            'message': 'Category retrieved successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        """
        Update a specific category (full update).
        """
        try:
            with transaction.atomic():
                category = self.get_object()
                serializer = self.get_serializer(category, data=request.data)
                
                if serializer.is_valid():
                    updated_category = serializer.save()
                    
                    return Response({
                        'status': 'success',
                        'message': 'Category updated successfully',
                        'data': serializer.data
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({
                        'status': 'error',
                        'message': 'Invalid data provided',
                        'errors': serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST)
                    
        except Category.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Category not found'
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error updating category: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def partial_update(self, request, *args, **kwargs):
        """
        Partially update a specific category.
        """
        try:
            with transaction.atomic():
                category = self.get_object()
                serializer = self.get_serializer(category, data=request.data, partial=True)
                
                if serializer.is_valid():
                    updated_category = serializer.save()
                    
                    return Response({
                        'status': 'success',
                        'message': 'Category partially updated successfully',
                        'data': serializer.data
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({
                        'status': 'error',
                        'message': 'Invalid data provided',
                        'errors': serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST)
                    
        except Category.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Category not found'
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error updating category: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def destroy(self, request, *args, **kwargs):
        """
        Delete a specific category.
        """
        with transaction.atomic():
            category = self.get_object()
            category_name = category.category_name
            category.delete()
            
            return Response({
                'status': 'success',
                'message': f'Category "{category_name}" deleted successfully'
            }, status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=False, methods=['get'])
    def active(self, request, org_id=None):
        """
        List only active categories.
        """
        try:
            active_categories = Category.objects.filter(is_active=True)
            serializer = self.get_serializer(active_categories, many=True)
            
            return Response({
                'status': 'success',
                'message': 'Active categories retrieved successfully',
                'data': serializer.data,
                'count': active_categories.count()
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error retrieving active categories: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=True, methods=['post'])
    def toggle_status(self, request, pk=None, org_id=None):
        """
        Toggle the active status of a category.
        """
        with transaction.atomic():
            category = self.get_object()
            category.is_active = not category.is_active
            category.save()
            
            serializer = self.get_serializer(category)
            
            status_text = 'activated' if category.is_active else 'deactivated'
            
            return Response({
                'status': 'success',
                'message': f'Category "{category.category_name}" {status_text} successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)





