from .base import *
import os

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogdb',
        'USER': 'admin',
        'PASSWORD': 'Rhoden5130!',
#いつかRDSに分けた時用        'HOST': 'blogdb.caa7627qv4ac.ap-northeast-1.rds.amazonaws.com',
        'HOST': 'ip-172-31-45-127.ap-northeast-1.compute.internal',
        'PORT': '3306',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATICFILES_DIRS = [
#   os.path.join(BASE_DIR, "static")
#]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')