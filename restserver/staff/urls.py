from django.urls import path
from .views import StaffListView

urlpatterns = [
    path('staff/', StaffListView.as_view()),  # List and create staff
    path('create-staff/', StaffListView.as_view()),  # Create a new product
    path('get-staff/<int:id>/', StaffListView.as_view()),  # Retrieve, update, and delete product by ID
    path('update-staff/<int:id>/', StaffListView.as_view()),  # Delete a specific product
    path('delete-staff/<int:id>/', StaffListView.as_view()),  # Delete a specific product
]

