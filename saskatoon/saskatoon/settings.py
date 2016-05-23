# coding: utf-8

"""
Django settings for saskatoon project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-ly1!%ui5z+*cfy9&wb=os6c(iysect2od0di1d$p(o$a696jo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'bootstrap3_datepicker',
    'suit',
    'dal',
    'dal_select2',
    'django_filters',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',
    'harvest',
    'member',
    'saskatoon',
    'django_extensions',
    'bootstrap3',
    'django_forms_bootstrap',
    'crispy_forms',
    'simple_history',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'saskatoon.urls'

APPEND_SLASH = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + '/saskatoon/templates/'
        ],
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

WSGI_APPLICATION = 'saskatoon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'saskatoon',
#        'USER': '',
#        'PASSWORD': '',
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
from django.core.urlresolvers import reverse_lazy

AUTH_USER_MODEL = "member.AuthUser"

LOGIN_URL = reverse_lazy('pages:login')

LOGIN_REDIRECT_URL = reverse_lazy('pages:index')


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
from django.utils.translation import gettext_lazy as _

LANGUAGE_CODE = 'fr-ca'

TIME_ZONE = 'America/Montreal'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('fr', u'Français'),
    ('en', u'English'),
)

LOCALE_PATHS = [
    'harvest/locale/',
    'member/locale/',
    'pages/locale/',
    'saskatoon/locale/'
]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'saskatoon/static')

STATIC_URL = '/static/'

# BOOTSRATP 3

BOOTSTRAP3 = {
    'success_css_class': '',
}

# SUIT CONFIG

SUIT_CONFIG = {
    'ADMIN_NAME': 'Saskatoon',
    'MENU_EXCLUDE': ('auth.group', 'auth'),
    }
