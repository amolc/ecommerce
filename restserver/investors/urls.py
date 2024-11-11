from django.urls import path
from .views import RegisterInvestorViews, AuthenticateInvestor, InvestorViews

urlpatterns = [
    
    # Investor routes
    path("create-investor/", RegisterInvestorViews.as_view()),
    path("login-investor/", AuthenticateInvestor.as_view()),
    path("get-investor/", InvestorViews.as_view()),
    path("update-investor/<int:id>/", InvestorViews.as_view()),
    path("delete-investor/<int:id>/", InvestorViews.as_view()),
]
