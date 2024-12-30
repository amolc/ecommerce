from django.urls import path
from .views import OrderItemView

urlpatterns = [
    path('orderItem/', OrderItemView.as_view()),
    path('create-orderItem/', OrderItemView.as_view()),
    path('get-orderItem/<int:id>/', OrderItemView.as_view()),
    path('update-orderItem/<int:id>/', OrderItemView.as_view()),
    path('delete-orderItem/<int:id>/', OrderItemView.as_view()),
]
