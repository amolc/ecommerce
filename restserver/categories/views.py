from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    Full CRUD for categories:
    - GET / → list all
    - GET /<id>/ → retrieve single
    - POST / → create
    - PUT /<id>/ → update entire
    - PATCH /<id>/ → partial update
    - DELETE /<id>/ → delete
    """
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
