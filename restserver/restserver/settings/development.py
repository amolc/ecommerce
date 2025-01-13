from .base import *  # type: ignore # noqa: F403 F401

CORS_ALLOW_ALL_ORIGINS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'flipopo_dev',
        'USER': 'flipopo_dev',
        'PASSWORD': '!Xdasdf890',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
