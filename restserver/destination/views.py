# views.py
import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DestinationSerializer
from .models import Destination
from common.utils import StayVillasResponse

class DestinationViews(APIView):

    def get(self, request, id=None, org_id=None):
            if id:
                item = Destination.objects.get(id=id)
                serializer = DestinationSerializer(item)
                return Response(
                    {"status": "success", "data": serializer.data},
                    status=status.HTTP_200_OK,
                )
            else:
                items = Destination.objects.all()
                serializer = DestinationSerializer(items, many=True)
                return Response(
                    {"status": "success", "data": serializer.data},
                    status=status.HTTP_200_OK,
                )
    
    

    def post(self, request, org_id=None):
        print("line 18",request.data)

        request_data = request.data.copy()
        request_data["org_id"] = org_id

        serializer_class = DestinationSerializer(data=request_data)

        if serializer_class.is_valid():
            serializer_class.save()
            api_response = Response(serializer_class.data, status=status.HTTP_201_CREATED)
        else:
            api_response = Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)     

        return api_response
        

    def patch(self, request, id=None, org_id=None):
        request_data = request.data
        request_data["org_id"] = org_id

        print("line 46",request_data)
        if not id:
            return Response({'status': 'error', 'message': 'ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)
        print("line 49",id)
        item = Destination.objects.get(id=id)
        print("line 51",item)
        serializer = DestinationSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        print("line ",serializer.data)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


    # Delete a customer
    def delete(self, request, id=None, org_id=None):
        request_data = request.data
        request_data["org_id"] = org_id
        # print("line 146",id)
        if not id:
            return Response({'status': 'error', 'message': 'ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)
        
        item = Destination.objects.get(id=id)
        print("line 151",id)
        print("line 151",item)
        item.delete()
        print("line 153",item)
        return Response({'status': 'success', 'message': 'Destination deleted successfully'}, status=status.HTTP_204_NO_CONTENT)