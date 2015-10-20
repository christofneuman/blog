# coding: utf-8
from blog.settings import *

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kylliki',
    }
}

# E-mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_HOST_USER = 'christof@namespace.ee'
EMAIL_HOST_PASSWORD = 'qSqMN_ZdtE5a1LbHLyGlSw'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
