from django.urls import path
from .views import (
    CategoryListCreateView,
    CategoryDetailView,
    SubCategoryListCreateView,
    SubCategoryDetailView,
)

urlpatterns = [
    # Categories
    path("", CategoryListCreateView.as_view(), name="category-list-create"),
    path("<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),

    # Subcategories
    path("<int:category_id>/subcategories/", SubCategoryListCreateView.as_view(), name="subcategory-list-create"),
    path("<int:category_id>/subcategories/<int:pk>/", SubCategoryDetailView.as_view(), name="subcategory-detail"),
]

