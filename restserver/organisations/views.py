from rest_framework.viewsets import (  # type: ignore
    ModelViewSet
)

from .models import (
    Organisation
)


class OrganisationViewSet(ModelViewSet):
    model = Organisation
