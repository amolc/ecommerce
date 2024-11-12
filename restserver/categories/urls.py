from django.urls import path
from .views import CategoryAPIView

urlpatterns = [
    # Destination routes
    path('categories/', CategoryAPIView.as_view()),  
    path('create-categories/', CategoryAPIView.as_view()), 
    path('categories/<int:category_id>/', CategoryAPIView.as_view()),  
    path('delete-categories/<int:category_id>/', CategoryAPIView.as_view()),  


]
