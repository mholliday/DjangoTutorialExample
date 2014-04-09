"""
Django settings for DjangoTutorialExample project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n6okc62oc3pxp^o6jednr_v#8-5jh81@c(!pp&3^tt^@2%^n5='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'DjangoTutorialExample.urls'

WSGI_APPLICATION = 'DjangoTutorialExample.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'holliday',
         'USER': 'holliday',
         'HOST': '127.0.0.1',
         'PASSWORD': '12345',
         'PORT': '5432',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# mh_29march2014: the code from here on to next dated comment
# added as directed in the Getting
# Started with Django on Heroku webpage
# The first step is to specify the location of the postgres database instance that heroku
# is using. This location is a url that can be found from the command prompt by the command
# heroku configure
# or it can be found by logging into the heroku.com website and clicking on the link named
# Databases at the top. Then choose the heroku project you are using from the list. 
# The configuration setting page lists a Host attribute, a Database attribute, a User attribute,
# a Port attribute, and a Password attribute (need to click show to see the Password).
# These values make up the url in the order of User:Password@Host:Port/Database with including
# the Port optional if the Port is the default which is 5432.
# 
# The documentation says to update the value of the key `default' in the DATABASES
# dictionary from environment variable you are supposed to create named $DATABASE_URL
# Instead I put the url of the postgres location hard-coded as an argument to the call to the
# dj_database_url.config function.
# Even though this is reassigning to the `default' value I can still run the project/app locally
# at 0.0.0.0:5000; I think it is accessing the heroku copy of postgres, not the copy on the local
# machine.
import dj_database_url
DATABASES['default'] = dj_database_url.config(
default='postgres://kthfdxmthlnlzg:fICHV8pQON7zjdOFLm5xsFuI0e@ec2-54-225-101-64.compute-1.amazonaws.com:5432/d2qvoj9qr78ir4')

# Honor the 'X-Forwarded-Proto' header for request_is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URLS = '/static/'

STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'static'),
)

