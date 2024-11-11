from django.urls import path
from .views import DestinationViews

urlpatterns = [
    # Destination routes
    path('destinations/', DestinationViews.as_view()),  # GET all destinations or POST to create a destination
    path('create-destinations/', DestinationViews.as_view()), 
    path('destinations/<int:id>/', DestinationViews.as_view()),  # GET, PATCH, DELETE a destination by ID
]

