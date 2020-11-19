from core.settings import *

DEBUG = False

assert SECRET_KEY is not None, "Please provide DJANGO_SECRET_KEY env variable with value"

ALLOWED_HOSTS +=[
  os.getenv("DJANGO_ALLOWED_HOSTS"),
]

DATABASES["default"].update({
  "ENGINE": "django.db.backends.postgresql"
  "NAME": os.getenv("DJANGO_DB_NAME"),
  "USER": os.getenv("DJANGO_DB_USER")
  "PASSWORD": os.getenv("DJANGO_DB_PASSWORD"),
  "HOST": os.getenv("DJANGO_DB_HOST"),
  "PORT": os.getenv("DJANGO_DB_PORT"),
})

CACHES = {
  "default": {
    "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    "LOCATION": "default-locmemcache",
    "TIMEOUT": int(os.getenv("DJANGO_CACHE_TIMEOUT"),),
  }
}


