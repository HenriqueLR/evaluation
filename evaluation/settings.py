#encoding: utf-8

'''
More informations you can see documentation 
of the project https://github.com/HenriqueLR/evaluation
'''

import os.path
VAR_ROOT = os.path.dirname(os.path.abspath(__file__))



ADMINS = (
    ('Henrique Luz Rodrigues', 'henrique.lr89@gmail.com'),
)

MANAGERS = ADMINS

DEBUG = True

TEMPLATE_DEBUG = DEBUG

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_ROOT, 'evaluation.sqlite'),
    }
}


SECRET_KEY = '++2h!_s8hwb7-_d*d1zs=bb9(ne9@+)=1zr^p5vfusxddm54n)'


MEDIA_ROOT = os.path.join(VAR_ROOT,'media')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(VAR_ROOT,'static_files')

STATIC_URL = '/static/'

STATICFILES_DIRS = (

        os.path.join(VAR_ROOT,'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
        os.path.join(VAR_ROOT,'templates'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'seek',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
'django.contrib.auth.context_processors.auth',
'django.core.context_processors.debug',
'django.core.context_processors.i18n',
'django.core.context_processors.media',
'django.core.context_processors.static',
'django.contrib.messages.context_processors.messages',
'django.core.context_processors.request',
)

ROOT_URLCONF = 'evaluation.urls'

WSGI_APPLICATION = 'evaluation.wsgi.application'

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


EMAIL_HOST = 'server email'
#EMAIL_HOST_PASSWORD = 'password' 
EMAIL_PORT = 25
EMAIL_USE_TLS = False
EMAIL_HOST_USER= 'user@example.com'

