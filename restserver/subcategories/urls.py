from django.urls import path
from .views import SubcategoryViews

urlpatterns = [
    path('subcategories/', SubcategoryViews.as_view()),  # List and create subcategories
    path('create-subcategories/', SubcategoryViews.as_view()),  # List and create subcategories
    path('subcategories/<int:id>/', SubcategoryViews.as_view()),  # Retrieve, update, and delete a specific subcategory by ID
    path('delete-subcategories/<int:id>/', SubcategoryViews.as_view()),  # Retrieve, update, and delete a specific subcategory by ID

]
