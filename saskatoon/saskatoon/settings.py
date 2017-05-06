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
from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-ly1!%ui5z+*cfy9&wb=os6c(iysect2od0di1d$p(o$a696jo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'crequest',
    'bootstrap3_datepicker',
    'dal',
    'dal_select2',
    'django_filters',
    'modeltranslation',
    'ckeditor',
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
    'django.contrib.humanize',
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
    'crequest.middleware.CrequestMiddleware',
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
                'django.core.context_processors.media',
                'saskatoon.context_processor.get_number_notification',
            ],
        },
    },
]

WSGI_APPLICATION = 'saskatoon.wsgi.application'


# USE MySQL for your local tests

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'saskatoon_dev',
        'USER': 'root',
<<<<<<< HEAD
        'PASSWORD': 'FDgwBoom!',
=======
        'PASSWORD': 'qqCXmHsj27',
>>>>>>> 4d75d7854073f46b8ae7af5c977990d831039689
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
AUTH_USER_MODEL = "member.AuthUser"

LOGIN_URL = reverse_lazy('pages:login')

LOGIN_REDIRECT_URL = reverse_lazy('pages:index')


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
# http://django-modeltranslation.readthedocs.io/en/latest/installation.html

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

MODELTRANSLATION_TRANSLATION_FILES = (
    'harvest.translation',
    'member.translation',
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'saskatoon/static')

STATIC_URL = '/static/'

# Media files (uploaded files, images)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

# BOOTSRATP 3

BOOTSTRAP3 = {
    'success_css_class': '',
}

# SUIT CONFIG

SUIT_CONFIG = {
    'ADMIN_NAME': 'Saskatoon',
    'MENU_EXCLUDE': ('auth.group', 'auth'),
    }

FILTERS_HELP_TEXT_FILTER = False

# EMAIL #

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
<<<<<<< HEAD
EMAIL_HOST_USER = 'lesfruitsdefendus.montreal@gmail.com'
EMAIL_HOST_PASSWORD = 'SR3112syrup'
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
=======
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
>>>>>>> 4d75d7854073f46b8ae7af5c977990d831039689

# CKEDITOR_UPLOAD_PATH = 'content/ckeditor/'

CKEDITOR_CONFIGS = {
    'default': {
        # 'toolbar': [
        # [      'Undo', 'Redo',
        # '-', 'Bold', 'Italic', 'Underline',
        # '-', 'Link', 'Unlink', 'Anchor',
        # '-', 'Format',
        # '-', 'SpellChecker', 'Scayt',
        # '-', 'Maximize',
        # ],
        # ],
        'width': 'auto',
        'height': 'auto',
        'toolbarCanCollapse': True,
    },
    'simple_toolbar': {
        'toolbar': [
            ['Bold', 'Italic', 'Underline'],
        ],
        'width': 840,
        'height': 300,
    },
}
