from django.urls import path
from .views import EnquiryViews

urlpatterns = [
    path('create-enquiry/', EnquiryViews.as_view()),  # POST
    path('get-enquiry/<int:id>/', EnquiryViews.as_view()),  # GET by ID
    path('get-enquiry/', EnquiryViews.as_view()),  # GET all
    path('update-enquiry/<int:id>/', EnquiryViews.as_view()),  # PATCH
    path('delete-enquiry/<int:id>/', EnquiryViews.as_view()),  # DELETE
]
