from pathlib import Path
import os
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config('SECRET_KEY')

DEBUG = False   ## Debug false in production mode

ALLOWED_HOSTS = ['localhost','127.0.0.1']  ## Input domain name in allowed hosts

## Display JSON only and hide browsable API for security.
REST_FRAMEWORK = {          
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'       ## Read-Only Security Permission
    ],
    'DEFAULT_RENDERER_CLASSES': (       ## Display JSON format
        'rest_framework.renderers.JSONRenderer',
    )
}



INSTALLED_APPS = [
    'django.contrib.admin',  ## Default Admin Panel by Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',      ## Django App Created by Developer
    'rest_framework',   ## Django Rest Framework Module
    'phonenumber_field',    ## Phone number field in models.py
   ## 'debug_toolbar',      ## Toolbar to check the performance
]

## Toolbar can access the Provided IP Address
''' 
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
'''

MIDDLEWARE = [
##   "debug_toolbar.middleware.DebugToolbarMiddleware",      ## Toolbar debug to check performance
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['Template'],   ## Template directory included in settings
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

## PostgreSQL Database Configuration.
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': config('NAME'),
    'USER': ('Database_owner'),
    'PASSWORD': config('PASSWORD'),
    'HOST': config('HOST'),
    'PORT': (''),
    'OPTIONS': {
      'sslmode': 'require',
    },
  }
}

## SQLite Database is not used in production mode.
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
