from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView

# Create a router and register our ViewSet
router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

# URL patterns for the ViewSet
urlpatterns = [
    # ViewSet URLs (recommended approach)
    path('', include(router.urls)),
    
    # Alternative: Generic view URLs (for backward compatibility)
    # path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    # path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
]
