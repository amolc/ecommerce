from django.urls import path
from .views import Order_ItemView

urlpatterns = [
    path('orderItem/', Order_ItemView.as_view()),  # List and create order
    path('create-orderItem/', Order_ItemView.as_view()),  # Create a new product
    path('get-orderItem/<int:id>/', Order_ItemView.as_view()),  # Retrieve, update, and delete product by ID
    path('update-orderItem/<int:id>/', Order_ItemView.as_view()),  # Delete a specific product
    path('delete-orderItem/<int:id>/', Order_ItemView.as_view()),  # Delete a specific product
]
