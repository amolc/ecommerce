import os
from .base import *  # noqa: F403 F401

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('MYSQL_DB', 'ecommerce'),
        'USER': os.environ.get('MYSQL_USER', 'stockrobot'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', '10gXWOqeaf'),
        'HOST': os.environ.get('MYSQL_HOST', 'api.flipopo.com'),
        'PORT': os.environ.get('MYSQL_PORT', '5432'),  # Default MySQL port
    }
}
