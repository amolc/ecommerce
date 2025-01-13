from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import StoreViewSet

router = DefaultRouter()
router.register(r'stores', StoreViewSet, basename='store')

urlpatterns = [
    path('store/', StoreViewSet.as_view({'get': 'list'})),
    path('create-store/', StoreViewSet.as_view({'post': 'create'})), 
    path('update-store/<int:pk>/', StoreViewSet.as_view({'put': 'update'})),  
    path('get-store/<int:pk>/', StoreViewSet.as_view({'get': 'retrieve'})),  
    path('delete-store/<int:pk>/', StoreViewSet.as_view({'delete': 'destroy'})),  
]
