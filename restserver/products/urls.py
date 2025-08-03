from django.urls import path
from .views import (
    ProductAPIViews,
    ProductCategoryAPIViews,
    ProductSubcategoryAPIViews,
)

urlpatterns = [
    path('get-products/', ProductAPIViews.as_view()),
    path('create-products/', ProductAPIViews.as_view()),
    path('get-product/<int:id>/', ProductAPIViews.as_view()),
    path('update-products/<int:id>/', ProductAPIViews.as_view()),
    path('delete-products/<int:id>/', ProductAPIViews.as_view()),
    
    path('category/', ProductCategoryAPIViews.as_view()),  
    path('create-category/', ProductCategoryAPIViews.as_view()), 
    path('get-category/<int:category_id>/', ProductCategoryAPIViews.as_view()),  
    path('update-category/<int:category_id>/', ProductCategoryAPIViews.as_view()),  
    path('delete-category/<int:category_id>/', ProductCategoryAPIViews.as_view()),  

    path('subcategory/', ProductSubcategoryAPIViews.as_view()),
    path('create-subcategory/', ProductSubcategoryAPIViews.as_view()),
    path('get-subcategory/<int:category_id>/', ProductSubcategoryAPIViews.as_view()),
    path('update-subcategory/<int:id>/', ProductSubcategoryAPIViews.as_view()),
    path('delete-subcategory/<int:id>/', ProductSubcategoryAPIViews.as_view()),
]
