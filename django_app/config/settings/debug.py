from .base import *

config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']

# INSTALLED_APPS
INSTALLED_APPS.append('django_extensions')

# WSGI application
WSGI_APPLICATION = 'config.wsgi.application'

# STATIC URLS
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '.static_root')

# MEDIA URLS
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '.media')

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# print
print('@@@ DEBUG:', DEBUG)
print('@@@ ALLOWED_HOSTS:', ALLOWED_HOSTS)