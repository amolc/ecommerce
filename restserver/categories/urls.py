from django.urls import path
from .views import CategoryViewSet

category_list = CategoryViewSet.as_view({'get': 'list'})
category_detail = CategoryViewSet.as_view({'get': 'retrieve'})
category_create = CategoryViewSet.as_view({'post': 'create'})
category_update = CategoryViewSet.as_view({'put': 'update', 'patch': 'partial_update'})
category_delete = CategoryViewSet.as_view({'delete': 'destroy'})

urlpatterns = [
    path('get-categories/', category_list, name='get-categories'),
    path('get-category/<int:pk>/', category_detail, name='get-category'),
    path('create-category/', category_create, name='create-category'),
    path('update-category/<int:pk>/', category_update, name='update-category'),
    path('delete-category/<int:pk>/', category_delete, name='delete-category'),
]
