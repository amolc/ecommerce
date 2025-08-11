from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet

# Create a router and register our ViewSet
router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

# URL patterns for the ViewSet
urlpatterns = [
    # ViewSet URLs
    path('', include(router.urls)),
]
