from rest_framework.views import APIView  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status  # type: ignore

from django.shortcuts import get_object_or_404
from django.db.utils import (
    IntegrityError
)

from .models import (
    Category,
    Subcategory
)

from .serializers import (
    CategorySerializer,
    SubcategorySerializer
)


class CategoryAPIView(APIView):
    def get(self, request, org_id=None, category_id=None):
        if category_id:
            try:
                category = Category.objects.get(id=category_id)
                serializer = CategorySerializer(category)
                
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Category.DoesNotExist:
                print(f"Category with id {category_id} not found")
                return Response(
                    {"error": "Category not found"},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            categories = Category.objects.all()

            show_inactive = request.GET.get('show_inactive')

            if show_inactive:
                pass
            else:
                categories = categories.filter(
                    is_active=True
                )

            serializer = CategorySerializer(
                categories,
                many=True
            )

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

    def post(self, request, org_id, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, org_id, category_id, *args, **kwargs):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response(
                {"error": "Category not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CategorySerializer(
            category,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, org_id, category_id):
        try:
            category = Category.objects.get(id=category_id)
            category.delete()
            return Response(
                {"message": "Category deleted successfully"},
                status=status.HTTP_204_NO_CONTENT
            )
        except Category.DoesNotExist:
            return Response(
                {"error": "Category not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        except IntegrityError as ex:
            print(ex)
            return Response(
                {"error": (
                    "Category cannot be deleted because foreign tables "
                    "reference it as a foreign key."
                )},
                status=status.HTTP_404_NOT_FOUND
            )


class SubcategoryViews(APIView):
    def post(self, request, org_id):
        category_id = request.data.get('category_id')
        
        if not category_id:
            return Response(
                {"status": "error", "message": "Category ID is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        category = get_object_or_404(Category, id=category_id)

        request_data = request.data.copy()
        request_data['category'] = category.id
        request_data['org_id'] = org_id

        category_object = Category.objects.get(id=category.id)
        serializer = CategorySerializer(category_object)
        
        serializer = SubcategorySerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None, org_id=None, category_id=None):
        subcategories = Subcategory.objects.all()  # Default query

        if category_id:
            subcategories = subcategories.filter(category_id=category_id)

        serializer = SubcategorySerializer(subcategories, many=True)
        return Response(
            {"status": "success", "data": serializer.data},
            status=status.HTTP_200_OK
        )

    def patch(self, request, id=None, org_id=None, category_id=None):
        if not id:
            return Response(
                {'status': 'error', 'message': 'ID is required for update'},
                status=status.HTTP_400_BAD_REQUEST
            )

        subcategory = get_object_or_404(Subcategory, id=id)
        serializer = SubcategorySerializer(
            subcategory,
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
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id=None, org_id=None, category_id=None):
        if not id:
            return Response(
                {'status': 'error', 'message': 'ID is required for deletion'},
                status=status.HTTP_400_BAD_REQUEST
            )

        subcategory = get_object_or_404(Subcategory, id=id)
        subcategory.delete()

        return Response(
            {"status": "success", "message": "Subcategory deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
