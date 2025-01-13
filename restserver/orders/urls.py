from django.urls import path

from .views import (
    OrderViews,
    OrderItemViews,
    change_order_status
)


urlpatterns = [
    path('order/', OrderViews.as_view()),
    path('create-order/', OrderViews.as_view()),
    path('get-order/<int:order_id>/', OrderViews.as_view()),
    path('update-order/<int:order_id>/', OrderViews.as_view()),
    path('delete-order/<int:order_id>/', OrderViews.as_view()),
    path('change-order-status/<int:order_id>', change_order_status),
    
    path('orderItem/', OrderItemViews.as_view()),
    path('create-orderItem/', OrderItemViews.as_view()),
    path('get-orderItem/<int:id>/', OrderItemViews.as_view()),
    path('update-orderItem/<int:id>/', OrderItemViews.as_view()),
    path('delete-orderItem/<int:id>/', OrderItemViews.as_view()),    
]
