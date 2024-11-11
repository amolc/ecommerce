from django.urls import path
from .views import PropertyViews, PropertyImageViews, PropertySearchViews, PropertyFilterViews, PropertyTopFilterViews, PropertySortViews,PropertyAgentViews

urlpatterns = [
    # Property routes
    path('properties/', PropertyViews.as_view()),  # GET all properties  or POST to create a property
    path('properties/search', PropertySearchViews.as_view()),  # GET all properties  or POST to create a property
    path('properties/filter', PropertyFilterViews.as_view()),  # GET all properties  or POST to create a property
    path('properties/filters', PropertyTopFilterViews.as_view()),  # GET all properties  or POST to create a property
    path('properties/sort', PropertySortViews.as_view()),  # GET all properties  or POST to create a property
    path('properties/agent', PropertyAgentViews.as_view()),  # GET all properties  or POST to create a property
    path('properties/<int:id>/', PropertyViews.as_view()),  # GET, PATCH, DELETE a property by ID
    
    # Property image routes
    path('properties/<int:property_id>/images/', PropertyImageViews.as_view()),  # POST to upload images for a property
    path('properties/images/<int:image_id>/', PropertyImageViews.as_view()),  # DELETE a property image by image ID
]
