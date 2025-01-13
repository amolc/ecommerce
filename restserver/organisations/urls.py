from django.urls import (
    path,
    include
)

from rest_framework.routers import (  # type: ignore
    DefaultRouter,
)

from .views import (
    OrganisationViewSet,
)

router = DefaultRouter()

router.register(
    r'organisations',
    OrganisationViewSet
)

urlpatterns = [
    path('', include(router)),
]
