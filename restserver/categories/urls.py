from django.urls import path
from .views import CategoryAPIView

urlpatterns = [
    # Destination routes
    path('category/', CategoryAPIView.as_view()),  
    path('create-category/', CategoryAPIView.as_view()), 
    path('get-category/<int:category_id>/', CategoryAPIView.as_view()),  
    path('update-category/<int:category_id>/', CategoryAPIView.as_view()),  
    path('delete-category/<int:category_id>/', CategoryAPIView.as_view()),  



]
