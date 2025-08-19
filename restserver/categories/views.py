from rest_framework import generics
from .models import Category, SubCategory
from .serializers import CategorySerializer, SubCategorySerializer


# Category List + Create
class CategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        org_id = self.kwargs["org_id"]
        return Category.objects.filter(organisation_id=org_id)

    def perform_create(self, serializer):
        org_id = self.kwargs["org_id"]
        serializer.save(organisation_id=org_id)


# Category Detail (Retrieve, Update, Delete)
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    lookup_field = "pk"

    def get_queryset(self):
        org_id = self.kwargs["org_id"]
        return Category.objects.filter(organisation_id=org_id)


# SubCategory List + Create
class SubCategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        category_id = self.kwargs["category_id"]
        return SubCategory.objects.filter(category_id=category_id)

    def perform_create(self, serializer):
        category_id = self.kwargs["category_id"]
        serializer.save(category_id=category_id)


# SubCategory Detail (Retrieve, Update, Delete)
class SubCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubCategorySerializer
    lookup_field = "pk"

    def get_queryset(self):
        category_id = self.kwargs["category_id"]
        return SubCategory.objects.filter(category_id=category_id)
