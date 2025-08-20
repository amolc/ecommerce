from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import SubCategory
from .serializers import SubCategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    """
    Full CRUD for subcategories:
    - GET / → list all
    - GET /<id>/ → retrieve single
    - POST / → create
    - PUT /<id>/ → update entire
    - PATCH /<id>/ → partial update
    - DELETE /<id>/ → delete
    """
    queryset = SubCategory.objects.all().order_by('id')
    serializer_class = SubCategorySerializer
    permission_classes = [AllowAny]
