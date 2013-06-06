
DEBUG = True
ALLOWED_HOSTS = ['*']

SECRET_KEY = ""

DATABASES['default'] =  dj_database_url.config()
