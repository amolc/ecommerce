# in-build
import traceback
import socket
# rest-framework
from rest_framework.response import Response
from rest_framework import status

# custom
# from customers.models import Logs


def Log(transaction_name, msg, Mode=None, userid=None):
    
    HOSTNAME = socket.gethostname()
    Logs.objects.create(
        transaction_name=transaction_name, mode=Mode, log_message=str(msg),
        user_id=userid,  
    )


class StayVillasResponse:

    @staticmethod
    def serializer_error(className, request, serializer, user_id=None):
        Ip = request.META['REMOTE_ADDR']
        error = serializer.errors
        if serializer.errors.get('non_field_errors'):
            error = serializer.errors.get('non_field_errors')[0]
        print("---------------------", traceback.format_exc(), error)
        msg = {'status': status.HTTP_400_BAD_REQUEST, 'message': error}

        Log(className, msg, request.method, user_id)
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def transaction_error(className, request, error, user_id=None):
        Ip = request.META['REMOTE_ADDR']
        msg = {'status': status.HTTP_400_BAD_REQUEST, 'message': error}
        Log(className, msg, request.method, user_id)
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def exception_error(className, request, e, user_id=None):
        log_msg = {'error': str(e), 'traceback': traceback.format_exc()}
        print("------------log_msg---------", log_msg)
        Log(className, log_msg, request.method, user_id)
        error = {'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message':"Something went wrong"}
        return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


