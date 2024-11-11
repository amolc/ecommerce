from django.urls import path
from .views import BookingViews, EventBookingViews, GuestViews

urlpatterns = [
    path('create-booking/', BookingViews.as_view()),  # POST
    path('get-booking/<int:id>/', BookingViews.as_view()),  # GET by ID
    path('get-bookings/', BookingViews.as_view()),  # GET all (for a specific org_id)
    path('update-booking/<int:id>/', BookingViews.as_view()),  # PATCH
    path('delete-booking/<int:id>/', BookingViews.as_view()),  # DELETE

    path('create-event-booking/', EventBookingViews.as_view()),  # POST
    path('get-event-booking/<int:id>/', EventBookingViews.as_view()),  # GET by ID
    path('get-event-bookings/', EventBookingViews.as_view()),  # GET all (for a specific org_id)
    path('update-event-booking/<int:id>/', EventBookingViews.as_view()),  # PATCH
    path('delete-event-booking/<int:id>/', EventBookingViews.as_view()),  # DELETE

    path('create-guest/', GuestViews.as_view(), name='create-guest'),  # POST
    path('get-guest/<int:id>/', GuestViews.as_view(), name='get-guest'),  # GET by ID
    path('get-guests/', GuestViews.as_view(), name='get-guests'),  # GET all
    path('update-guest/<int:id>/', GuestViews.as_view(), name='update-guest'),  # PATCH
    path('delete-guest/<int:id>/', GuestViews.as_view(), name='delete-guest'),  # DELETE
]
