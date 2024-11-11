from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import eventdata
from .serializers import EventSerializer

class EventViews(APIView):

    def post(self, request, org_id=None):
        # Add org_id to the request data if needed
        request_data = request.data.copy()
        request_data['org_id'] = org_id  # Assuming org_id is part of the event data

        serializer = EventSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None, org_id=None):
        if id:
            # Fetch a specific event by ID
            event = get_object_or_404(eventdata, id=id)  # Corrected to use 'eventdata'
            serializer = EventSerializer(event)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        # Fetch all events if no ID is provided
        events = eventdata.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None, org_id=None):
        if not id:
            return Response({'status': 'error', 'message': 'ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)

        event = get_object_or_404(eventdata, id=id)  # Corrected to use 'eventdata'
        serializer = EventSerializer(event, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, org_id=None):
        if not id:
            return Response({'status': 'error', 'message': 'ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)

        event = get_object_or_404(eventdata, id=id)
        event.delete()
        return Response({"status": "success", "message": "Event deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
