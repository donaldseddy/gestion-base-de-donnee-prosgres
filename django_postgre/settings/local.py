from .base import *
from .base import config

DEBUG = True
ALLOWED_HOSTS = ['localhost']

DATABASES = {
    
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': config("DATABASE_NAME"),
        'USER': config("DATABASE_USER"),
        'PASSWORD': config("DATABASE_PASSWORD"),
        'HOST': config("DATABASE_HOST"),
        'PORT': '5432',
    }
}