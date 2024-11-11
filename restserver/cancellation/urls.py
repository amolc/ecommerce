from django.urls import path
from .views import CancellationViews

urlpatterns = [
    path('create-cancellation/', CancellationViews.as_view()),  # POST
    path('get-cancellation/<int:id>/', CancellationViews.as_view()),  # GET by ID
    path('get-cancellation/', CancellationViews.as_view()),  # GET all
    path('update-cancellation/<int:id>/', CancellationViews.as_view()),  # PATCH
    path('delete-cancellation/<int:id>/', CancellationViews.as_view()),  # DELETE
]
