from django.urls import path
from .views import PropertyListingViews

urlpatterns = [
    # Property listing routes
    path("create-property_list/", PropertyListingViews.as_view()),
    path("get-property_list/<int:id>/", PropertyListingViews.as_view()),
    path("get-property_list/", PropertyListingViews.as_view()),
    path("update-property_list/<int:id>/", PropertyListingViews.as_view()),
    path("delete-property_list/<int:id>/", PropertyListingViews.as_view()),
]
