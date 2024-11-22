from django.urls import path
from .views import BillingViews

urlpatterns = [
    path('create-billing/', BillingViews.as_view()),  # POST
    path('get-billing/<int:id>/', BillingViews.as_view()),  # GET by ID
    path('get-billing/', BillingViews.as_view()),  # GET all (for a specific org_id)
    path('update-billing/<int:id>/', BillingViews.as_view()),  # PATCH
    path('delete-billing/<int:id>/', BillingViews.as_view()),  # DELETE


]