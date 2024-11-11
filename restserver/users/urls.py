# django
from django.urls import path
from .views import RegisterUserView, UserView

urlpatterns = [
    path('register-user/', RegisterUserView.as_view()),  
    #path('login-user/', AuthenticateUser.as_view()),       
    path('users/', UserView.as_view()),                
    path('users/<int:id>/', UserView.as_view()),
]
