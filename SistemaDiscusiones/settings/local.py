from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Discusiones',
        'USER': 'cursodjango',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

SOCIAL_AUTH_FACEBOOK_KEY = '894701700556242'
SOCIAL_AUTH_FACEBOOK_SECRET = '66b7950219e2863930e64a140e147f1a'

SOCIAL_AUTH_TWITTER_KEY = '43BoDB8nQOsxkiAwPhWyogar5'
SOCIAL_AUTH_TWITTER_SECRET = 'w1gwBHQSnZFCDfDC6mzx43ojCXt7zpUczBOKxGgdKgyaReb4O2'