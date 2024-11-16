from django.urls import path
from .views import  AdminViews, RegisterAdminViews, LoginViews, AgentFilterViews
urlpatterns = [
    # Agent routes
    path("create-admin/", RegisterAdminViews.as_view()),
    path("login-admin/", LoginViews.as_view()),
    path("get-admin/", AdminViews.as_view()),
    path("get-admin/<int:id>/", AgentFilterViews.as_view()),
    path("update-admin/<int:id>/", AdminViews.as_view()),
    path("delete-admin/<int:id>/", AdminViews.as_view()),
]
