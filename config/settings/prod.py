from .base import *

DEBUG = False
ALLOWED_HOSTS = env_config("DJANGO_ALLOWED_HOSTS", default="myapp.com").split(",")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env_config("POSTGRES_DB"),
        "USER": env_config("POSTGRES_USER"),
        "PASSWORD": env_config("POSTGRES_PASSWORD"),
        "HOST": env_config("POSTGRES_HOST"),
        "PORT": env_config("POSTGRES_PORT", default="5432"),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env_config('SMTP_HOST')
EMAIL_PORT = int(env_config('SMTP_PORT'))
EMAIL_USE_TLS = bool(env_config('SMTP_TLS'))
EMAIL_USE_SSL = bool(env_config('SMTP_SSL'))
EMAIL_HOST_USER = env_config('SMTP_USERNAME')
EMAIL_HOST_PASSWORD = env_config('SMTP_PASSWORD')
