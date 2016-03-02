import os

"""
Main Settings
"""
DEBUG = True
ALLOWED_HOSTS = []
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LM_API_URL = 'http://localhost:4000/api/' # Lead Manager API URL
LM_API_TOKEN = '3294107ac55a318f1c7d9b8ee380c28f1979fa7a' # Lead Manager API Token


"""
Database
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

"""
Static files
"""
STATIC_URL = '/static/'
STATIC_PATH = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = (
    STATIC_PATH,
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')