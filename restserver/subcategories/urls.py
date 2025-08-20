from rest_framework.routers import DefaultRouter
from .views import SubCategoryViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'', SubCategoryViewSet, basename='subcategory')

urlpatterns = [
    path('', include(router.urls)),
]
