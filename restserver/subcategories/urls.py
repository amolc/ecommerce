from django.urls import path
from .views import SubcategoryViewSet

subcategory_list = SubcategoryViewSet.as_view({'get': 'list'})
subcategory_detail = SubcategoryViewSet.as_view({'get': 'retrieve'})
subcategory_create = SubcategoryViewSet.as_view({'post': 'create'})
subcategory_update = SubcategoryViewSet.as_view({'put': 'update', 'patch': 'partial_update'})
subcategory_delete = SubcategoryViewSet.as_view({'delete': 'destroy'})

urlpatterns = [
    path('get-subcategories/', subcategory_list, name='get-subcategories'),
    path('get-subcategory/<int:pk>/', subcategory_detail, name='get-subcategory'),
    path('create-subcategory/', subcategory_create, name='create-subcategory'),
    path('update-subcategory/<int:pk>/', subcategory_update, name='update-subcategory'),
    path('delete-subcategory/<int:pk>/', subcategory_delete, name='delete-subcategory'),
]
