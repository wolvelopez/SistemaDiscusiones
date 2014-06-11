from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)

SECRET_KEY = '2f#rl*m_*h2+-&27*)l+7oc=n4@(wtbz@g*)bf6(c4^y8h+d@y'

DJANGO_APPS = (
	'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'south',
    'social.apps.django_app.default',
)

LOCAL_APPS = (
	'apps.home',
    'apps.users',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
   

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'SistemaDiscusiones.urls'

WSGI_APPLICATION = 'SistemaDiscusiones.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [BASE_DIR.child('templates')]

AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = (
        'social.backends.facebook.FacebookAppOAuth2',
        'social.backends.facebook.FacebookOAuth2',
        'social.backends.twitter.TwitterOAuth',
        'django.contrib.auth.backends.ModelBackend',
    )

#A donde va si todo sale bien
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
#A donde va si hay error
SOCIAL_AUTH_LOGIN_URL = '/error/'
#Utiliza el modelo que hemos creado nosotros en la app users
SOCIAL_AUTH_USER_MODEL = 'users.User'
#Facebook nos da el email de usuario
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

#Utilizartemos pipelines para traer la foto de usuario
SOCIAL_AUTH_PIPELINES = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    #Esta es la que creamos nosotros
    'apps.users.pipelines.get_avatar',
)