from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Subcategory
from .serializers import SubcategorySerializer

class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.select_related('category').all().order_by('id')
    serializer_class = SubcategorySerializer
    permission_classes = [AllowAny]
