from django.urls import path
from .views import InventoryViews

urlpatterns = [
    path('inventory/', InventoryViews.as_view(), name='inventory-list'),  # Fetch all or add inventory
    path('inventory/<int:product_id>/', InventoryViews.as_view(), name='inventory-detail'),  # Specific inventory
]
