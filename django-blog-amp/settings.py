from django.core.management.utils import get_random_secret_key
from pathlib import Path
import os
import sys
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secret_key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django-blog-amp-app',
    'crispy_forms',
    'django_social_share',
    'django_summernote',
    'django.contrib.sitemaps',
    'corsheaders',
    'captcha',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

#CORS_ORIGIN_WHITELIST = (
#  'http://localhost:8000',
#)

ROOT_URLCONF = 'django-blog-amp.urls'

TEMPLATES_DIRS = os.path.join(BASE_DIR,'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIRS],
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

WSGI_APPLICATION = 'django-blog-amp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
# DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"

"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}"""

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR/'db.sqlite3',
    }
}
"""

DATABASES={
   'default':{
      'ENGINE':'django.db.backends.postgresql',
      'NAME':os.getenv('DATABASE_NAME'),
      'USER':os.getenv('DATABASE_USER'),
      'PASSWORD':os.getenv('DATABASE_PASSWORD'),
      'HOST':os.getenv('DATABASE_HOST'),
      'PORT':'5432',
   }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
MEDIA_URL = '/media/'

X_FRAME_OPTIONS = 'SAMEORIGIN'

STATIC_URL = "/static/"
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT  = os.path.join(BASE_DIR, 'staticfiles')
# Uncomment if you have extra static files and a directory in your GitHub repo.
# If you don't have this directory and have this uncommented your build will fail
# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
CRISPY_TEMPLATE_PACK = 'bootstrap4'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

RECAPTCHA_PUBLIC_KEY = "6LeERfQhAAAAAK3V2AmqHWBUJpHJzdoHZccyrTJb"
RECAPTCHA_PRIVATE_KEY = "6LeERfQhAAAAAGD6CPGKyO4PatVYDxO2y708N-5l"

CSRF_TRUSTED_ORIGINS = ['https://regiapriandi.me']
