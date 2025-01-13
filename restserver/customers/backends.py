import re

from django.contrib.auth.backends import (
    BaseBackend
)

def is_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    match = re.match(pattern, email)
    return match is not None

class CustomerBackend(BaseBackend):
    pass
