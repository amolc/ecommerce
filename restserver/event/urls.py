from django.urls import path
from .views import EventViews

urlpatterns = [
    path('create-event/', EventViews.as_view()),  # POST
    path('get-event/<int:id>/', EventViews.as_view()),  # GET by ID
    path('get-event/', EventViews.as_view()),  # GET all
    path('update-event/<int:id>/', EventViews.as_view()),  # PATCH
    path('delete-event/<int:id>/', EventViews.as_view()),  # DELETE
]
