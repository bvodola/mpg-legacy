import os

"""
Main Settings
"""
DEBUG = True
ALLOWED_HOSTS = [ 'localhost', '.mybluemix.net' ]
ADMINS = (('Brunno', 'bvodola@gmail.com'),)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LM_API_URL = 'http://lm.mediaplanning.com.br/api/' # Lead Manager API URL
LM_API_TOKEN = '81acf001fe50dd8a73eecade2225be6fc786eec0' # Lead Manager API Token

"""
Database
"""
#"uri_direct_1": "postgres://admin:TQZUQDWJDRKSSWEC@sl-us-south-1-portal.8.dblayer.com:22590/compose",
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'compose',
        'USER': 'admin',
        'PASSWORD': 'TQZUQDWJDRKSSWEC',
        'HOST': 'sl-us-south-1-portal.8.dblayer.com',
        'PORT': '22590',
    }
}

"""
Static files
"""
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATIC_PATH = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = (
    STATIC_PATH,
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

"""
E-mail settings
"""
# EMAIL_HOST = 'smtp.webfaction.com'
# EMAIL_HOST_USER = 'mpg_mail'
# EMAIL_HOST_PASSWORD = 'qZwX1001'
# DEFAULT_FROM_EMAIL = 'contato@mediaplanning.com.br'
# SERVER_EMAIL = 'contato@mediaplanning.com.br'
