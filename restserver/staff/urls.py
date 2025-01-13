from django.urls import path

from .views import (
    StaffViews,
    RegisterStaffViews,
    LoginViews,
    AgentFilterViews
)

urlpatterns = [
    path("create-admin/", RegisterStaffViews.as_view()),
    path("login-admin/", LoginViews.as_view()),
    path("get-admin/", StaffViews.as_view()),
    path("get-admin/<int:id>/", AgentFilterViews.as_view()),
    path("update-admin/<int:id>/", StaffViews.as_view()),
    path("delete-admin/<int:id>/", StaffViews.as_view()),
]
