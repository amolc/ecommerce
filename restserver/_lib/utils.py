from typing import (
    Dict,
    Any
)
import traceback

from rest_framework.serializers import (  # type: ignore
    Serializer,
)
from rest_framework.response import (  # type: ignore
    Response
)
from rest_framework.request import (  # type: ignore
    Request
)
from rest_framework import (  # type: ignore
    status
)

from customers.models import (  # type: ignore
    CustomerLog
)

def Log(
    transaction_name: str,
    msg: Dict[str, Any],
    Mode: str | None=None,
    userid: int | None=None
):
    CustomerLog.objects.create(
        transaction_name=transaction_name, mode=Mode, log_message=str(msg),
        user_id=userid,  
    )


class StayVillasResponse:
    @staticmethod
    def serializer_error(
        className: str,
        request: Request,
        serializer: Serializer,
        user_id: int | None=None
    ):
        error = serializer.errors
        if serializer.errors.get('non_field_errors'):
            error = serializer.errors.get('non_field_errors')[0]
        print("---------------------", traceback.format_exc(), error)
        msg = {'status': status.HTTP_400_BAD_REQUEST, 'message': error}

        Log(className, msg, request.method, user_id)
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def transaction_error(
        className: str,
        request: Request,
        error: str,
        user_id: int | None=None
    ):
        msg = {'status': status.HTTP_400_BAD_REQUEST, 'message': error}
        Log(className, msg, request.method, user_id)
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def exception_error(
        className: str,
        request: Request,
        e: str,
        user_id: int | None=None
    ):
        log_msg = {
            'error': str(e),
            'traceback': traceback.format_exc()
        }
        print("------------log_msg---------", log_msg)
        Log(className, log_msg, request.method, user_id)
        
        error = {
            'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'message':"Something went wrong"
        }
        
        return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
