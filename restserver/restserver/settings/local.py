from .base import *  # type: ignore # noqa: F403 F401

CORS_ALLOW_ALL_ORIGINS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pamosapicks',
        'USER': 'pamosapicks',
        'PASSWORD': '10gXWOqeaf!',
        'HOST': 'db.pamosapicks.com',
        'PORT': '3306'
    }
}
