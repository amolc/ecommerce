from django.urls import path
from .views import OrderView

urlpatterns = [
    path('orderItem/', OrderView.as_view()),  # List and create order
    path('create-orderItem/', OrderView.as_view()),  # Create a new product
    path('orderItem/<int:id>/', OrderView.as_view()),  # Retrieve, update, and delete product by ID
    path('delete-orderItem/<int:id>/', OrderView.as_view()),  # Delete a specific product
]
