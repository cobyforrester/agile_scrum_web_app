"""
Django settings for agile_scrum project.

Generated by 'django-admin startproject' using Django 2.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR is where manage.py is
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY_SCRUMMY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.environ.get('DEBUG_VALUE_SCRUMMY')=='True')

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'scrummy-backend.herokuapp.com']  #Add domain when established!!!
LOGIN_URL = '/login'
#information for projects
MAX_DESCRIPTION_LENGTH = 1000
MAX_TITLE_LENGTH = 50
MIN_DESCRIPTION_LENGTH = 20
MIN_TITLE_LENGTH = 3
PROJECT_MEMBERS_ACTION_OPTIONS = ['add', 'remove', 'view']

#information for sprints
MAX_GOAL_LENGTH = 1000
MIN_GOAL_LENGTH = 20

#information for tasks
MAX_DESCRIPTION_LENGTH_TASK = 1000
MIN_DESCRIPTION_LENGTH_TASK = 20
MAX_TITLE_LENGTH_TASK = 50
MIN_TITLE_LENGTH_TASK = 3

CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/.*$'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #third party
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'knox',
    #internal
    'sprints',
    'projects',
    'tasks',
    'accounts',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    #for cors headers
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'agile_scrum.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'agile_scrum.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'scrummy',
        'USER': os.environ.get('SCRUMMY_PSQL_USER'),
        'PASSWORD': os.environ.get('SCRUMMY_PSQL_PASS'),
        'HOST': 'localhost'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/





DEFAULT_RENDERER_CLASSES = ['rest_framework.renderers.JSONRenderer',]
if DEBUG:
    DEFAULT_RENDERER_CLASSES += ['rest_framework.renderers.BrowsableAPIRenderer']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',),
    'DEFAULT_RENDERER_CLASSES': DEFAULT_RENDERER_CLASSES,
}

django_heroku.settings(locals())