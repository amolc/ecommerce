from django.urls import path
from .views import OrderViews

urlpatterns = [
    path('order/', OrderViews.as_view()),  # List and create order
    path('create-order/', OrderViews.as_view()),  # Create a new product
    path('order/<int:id>/', OrderViews.as_view()),  # Retrieve, update, and delete product by ID
    path('delete-order/<int:id>/', OrderViews.as_view()),  # Delete a specific product
]
