import os

"""
Main Settings
"""
DEBUG = False
ALLOWED_HOSTS = ['.mediaplanning.com.br', '.mpg.net.br']
ADMINS = (('Brunno', 'bvodola@gmail.com'),)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LM_API_URL = 'http://lm.mediaplanning.com.br/api/' # Lead Manager API URL
LM_API_TOKEN = '81acf001fe50dd8a73eecade2225be6fc786eec0' # Lead Manager API Token

"""
Database
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mpg_db',
        'USER': 'bvodola',
        'PASSWORD': 'qZwX1001'
    }
}

"""
Static files
"""
STATIC_ROOT = '/home/bvodola/webapps/mpg_static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

"""
E-mail settings
"""
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'mpg_mail'
EMAIL_HOST_PASSWORD = 'qZwX1001'
DEFAULT_FROM_EMAIL = 'contato@mediaplanning.com.br'
SERVER_EMAIL = 'contato@mediaplanning.com.br'