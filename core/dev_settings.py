from core.settings import *

DEBUG = True
SECRET_KEY = "foo an anonym secret"

INSTALLED_APPS +=[
  "debug_toolbar",
]

MIDDLEWARE.insert(3, 'debug_toolbar.middleware.DebugToolbarMiddleware',)


CACHES = {
  "default": {
    "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    "LOCATION": "default-locmemcache",
    "TIMEOUT": 5,
  }
}

# Django Debug Toolbar
INTERNAL_IPS = [
  "127.0.0.1",
]