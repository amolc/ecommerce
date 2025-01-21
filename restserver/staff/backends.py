import re

from typing import (
    Any,
)

from rest_framework.request import (  # type: ignore
    Request
)
from django.contrib.auth.backends import (
    BaseBackend
)
from django.contrib.auth import (
    get_user_model
)


class EmailBackend(BaseBackend):
    def authenticate(
        self,
        request: Request,
        email: str | None=None,
        password: str | None=None,
        **kwargs: Any,
    ):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
            if password:
                if user.check_password(password):
                    return user
        except UserModel.DoesNotExist:
            return None

def is_email(email: str):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    match = re.match(pattern, email)
    return match is not None
