from django.urls import (
    path,
    include
)

from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    BannerAPIViews
)

router = DefaultRouter()

router.register(
    r'banner',
    BannerAPIViews
)

app_name = "site_content"
urlpatterns = [
    path('', include(router.urls)),
]
