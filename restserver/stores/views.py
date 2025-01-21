from rest_framework import viewsets  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework.request import Request  # type: ignore
from rest_framework.decorators import action  # type: ignore
from .models import Store
from .serializers import StoreSerializer

class StoreViewSet(viewsets.ModelViewSet):
    
    queryset = Store.objects.all()
    
    serializer_class = StoreSerializer
    
    #  creating a store 
    @action(detail=False, methods=['post'])
    def create_store(self, request: Request):
        return self.create(request)
    
    # updating a store
    @action(detail=True, methods=['put'])
    def update_store(self, request: Request, pk: int | None=None):
        store = self.get_object()  
        serializer = self.get_serializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    # fetch
    @action(detail=True, methods=['get'])
    def get_store(self, request: Request, pk: int | None=None):
        store = self.get_object()
        serializer = self.get_serializer(store)
        return Response(serializer.data)

    #deleting a store
    @action(detail=True, methods=['delete'])
    def delete_store(self, request: Request, pk: int | None=None):
        store = self.get_object()
        store.delete()
        return Response(status=204) 
