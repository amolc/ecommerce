from django.urls import path
from .views import ProductViews

urlpatterns = [
    path('products/', ProductViews.as_view()),  # List and create products
    path('create-products/', ProductViews.as_view()),  # Create a new product
    path('products/<int:id>/', ProductViews.as_view()),  # Retrieve, update, and delete product by ID
    path('delete-products/<int:id>/', ProductViews.as_view()),  # Delete a specific product
]
