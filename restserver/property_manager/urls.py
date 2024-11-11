from django.urls import path
from .views import PropertyManagerViews

urlpatterns = [
    path('create-property_manager/', PropertyManagerViews.as_view()),  # POST
    path('get-property_manager/<int:id>/', PropertyManagerViews.as_view()),  # GET by ID
    path('get-property_manager/', PropertyManagerViews.as_view()),  # GET all
    path('update-property_manager/<int:id>/', PropertyManagerViews.as_view()),  # PATCH
    path('delete-property_manager/<int:id>/', PropertyManagerViews.as_view()),  # DELETE
]
