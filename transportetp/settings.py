"""
Django settings for transportetp project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "rn0+t%+-0dkv!ix@4k%jw2s)x24is8o4@mrv3s1t$51l1i7li7"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.ruta",
    "apps.pasajero",
    'apps.vendor',
    "apps.transportista",
    "apps.manejadoqr",
    "apps.lectorQR",
    "apps.sites",
    "apps.viajes",
    "apps.login",
    "apps.account",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "transportetp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "plantillas")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

AUTH_USER_MODEL = "account.Account"
WSGI_APPLICATION = "transportetp.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#'default': {
# 'ENGINE': 'django.db.backends.sqlite3',
#'NAME': os.path.join(BASE_DIR, 'db.trasporte'),
# }
# }
import dj_database_url
from decouple import config

DATABASES = {"default": dj_database_url.config(default=config("DATABASE_URL"))}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "es-mx"

# TIME_ZONE = 'UTC'
TIME_ZONE = "Etc/GMT+6"  # esta es la hora para el salvador
# TIME_ZONE = 'Etc/GMT+4' #esta es la hora para el Republica Dominicana

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_URL = '/static/'
# STATICFILES_DIRS = (
#  os.path.join(BASE_DIR, 'static'),
# )

STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(BASE_DIR, "assets")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# apartado de registrations


LOGIN_REDIRECT_URL = "/home"
LOGOUT_REDIRECT_URL = "/login"

EMAIL_USER_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "tpgoapp@gmail.com"
EMAIL_HOST_PASSWORD = "Test_12345"
EMAIL_PORT = 587

"""EMAIL_BACKEND = (
    "django.core.mail.backends.console.EmailBackend"  # During development only
)"""
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "TPGO TEAM <tpgoapp@gmail.com>"

# configuraciones adicionales
SECURE_SSL_REDIRECT = True
