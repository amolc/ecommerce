from django.urls import path
from .views import (
    CategoryAPIView,
    SubcategoryViews
)

urlpatterns = [
    # Destination routes
    path('category/', CategoryAPIView.as_view()),  
    path('create-category/', CategoryAPIView.as_view()), 
    path('get-category/<int:category_id>/', CategoryAPIView.as_view()),  
    path('update-category/<int:category_id>/', CategoryAPIView.as_view()),  
    path('delete-category/<int:category_id>/', CategoryAPIView.as_view()),  

    path('subcategory/', SubcategoryViews.as_view()),  # List and create subcategories
    path('create-subcategory/', SubcategoryViews.as_view()),  # List and create subcategories
    path('get-subcategory/<int:category_id>/', SubcategoryViews.as_view()),  # Retrieve, update, and delete a specific subcategory by ID
    path('update-subcategory/<int:id>/', SubcategoryViews.as_view()),  # Retrieve, update, and delete a specific subcategory by ID
    path('delete-subcategory/<int:id>/', SubcategoryViews.as_view()),  # Retrieve, update, and delete a specific subcategory by ID

]
