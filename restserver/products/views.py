from django.shortcuts import (
    get_object_or_404
)
from django.core.paginator import (
    Paginator
)
from django.db.utils import (
    IntegrityError
)


from rest_framework.views import APIView  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status  # type: ignore

from .models import (
    Product,
    ProductCategory,
    ProductSubcategory
)

from .serializers import (
    ProductSerializer,
    ProductCategorySerializer,
    ProductSubcategorySerializer,    
)


class ProductAPIViews(APIView):
    def post(self, request, org_id=None):
        data = request.data
        categoryid = data['category']
        category_object = ProductCategory.objects.get(id=categoryid)
        serializer = ProductCategorySerializer(category_object)

        try:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

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

    def get(self, request, org_id=None, id=None):
        category_id = request.GET.get('category_id')
        page = request.GET.get('page')
        search = request.GET.get('search')

        if id:
            product = get_object_or_404(Product, id=id)
            serializer = ProductSerializer(product)
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK
            )

        # Otherwise, fetch products with optional filters
        products = Product.objects.all()

        if category_id is not None:
            products = products.filter(category_id=category_id)

        if search is not None:
            products = products.filter(product_name__icontains=search)

        paginator = Paginator(products, per_page=18)

        if page is not None:
            products_page = paginator.page(page)
        else:
            products_page = paginator.page(1)

        if not products.exists():
            return Response(
                {
                    "status": "success",
                    "data": [],
                    "message": "No products found for the given filters",
                    "num_pages": 0,
                    "start_index": 0,
                    "end_index": 0,
                    "current_page": 0
                },
                status=status.HTTP_200_OK
            )

        # Serialize and return the list of filtered products
        serializer = ProductSerializer(
            products_page.object_list,
            many=True
        )

        return Response(
            {
                "status": "success",
                "data": serializer.data,
                "page": page,
                "num_pages": paginator.num_pages,
                "start_index": products_page.start_index(),
                "end_index": products_page.end_index(),
                "current_page": products_page.number,
                "total_num_items": paginator.object_list.count(),
            },
            status=status.HTTP_200_OK
        )

    def patch(self, request, org_id=None, id=None):
        if not id:
            return Response(
                {'status': 'error', 'message': 'ID is required for update'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Attempt to fetch the product with both id and org_id
        product = Product.objects.filter(id=id).first()
        if not product:
            return Response(
                {"error": "Product not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProductSerializer(
            product,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE method to delete a product
    def delete(self, request, org_id, id):
        try:
            product = Product.objects.get(id=id)
            product.delete()
            return Response(
                {"message": "Category deleted successfully"},
                status=status.HTTP_204_NO_CONTENT
            )
        except Product.DoesNotExist:
            return Response(
                {"error": "Category not found"},
                status=status.HTTP_404_NOT_FOUND
            )


class ProductCategoryAPIViews(APIView):
    def get(self, request, org_id=None, category_id=None):
        if category_id:
            try:
                category = ProductCategory.objects.get(id=category_id)
                serializer = ProductCategorySerializer(category)
                
                return Response(serializer.data, status=status.HTTP_200_OK)
            except ProductCategory.DoesNotExist:
                print(f"Category with id {category_id} not found")
                return Response(
                    {"error": "Category not found"},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            categories = ProductCategory.objects.all()

            show_inactive = request.GET.get('show_inactive')

            if show_inactive:
                pass
            else:
                categories = categories.filter(
                    is_active=True
                )

            serializer = ProductCategorySerializer(
                categories,
                many=True
            )

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

    def post(self, request, org_id, *args, **kwargs):
        serializer = ProductCategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, org_id, category_id, *args, **kwargs):
        try:
            category = ProductCategory.objects.get(id=category_id)
        except ProductCategory.DoesNotExist:
            return Response(
                {"error": "Category not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProductCategorySerializer(
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
            category = ProductCategory.objects.get(id=category_id)
            category.delete()
            return Response(
                {"message": "Category deleted successfully"},
                status=status.HTTP_204_NO_CONTENT
            )
        except ProductCategory.DoesNotExist:
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


class ProductSubcategoryAPIViews(APIView):
    def post(self, request, org_id):
        category_id = request.data.get('category_id')
        
        if not category_id:
            return Response(
                {"status": "error", "message": "Category ID is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        category = get_object_or_404(ProductCategory, id=category_id)

        request_data = request.data.copy()
        request_data['category'] = category.id
        request_data['org_id'] = org_id

        # Try for error. TODO: Fix
        ProductCategory.objects.get(id=category.id)

        serializer = ProductSubcategorySerializer(data=request_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None, org_id=None, category_id=None):
        subcategories = ProductSubcategory.objects.all()  # Default query

        if category_id:
            subcategories = subcategories.filter(category_id=category_id)

        serializer = ProductSubcategorySerializer(subcategories, many=True)
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

        subcategory = get_object_or_404(ProductSubcategory, id=id)
        serializer = ProductSubcategorySerializer(
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

        subcategory = get_object_or_404(ProductSubcategory, id=id)
        subcategory.delete()

        return Response(
            {"status": "success", "message": "Subcategory deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
