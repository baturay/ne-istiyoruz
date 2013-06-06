
from mezzanine.project_template.settings import *
import os
import dj_database_url

# Paths
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIRNAME = PROJECT_ROOT.split(os.sep)[-1]
STATIC_ROOT = os.path.join(PROJECT_ROOT, STATIC_URL.strip("/"))
MEDIA_ROOT = os.path.join(PROJECT_ROOT, *MEDIA_URL.strip("/").split("/"))
ROOT_URLCONF = "%s.urls" % PROJECT_DIRNAME
TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)

USE_I18N = True
LANGUAGE_CODE = "tr_TR"

INSTALLED_APPS = (
    "main",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "mezzanine.boot",
    "mezzanine.conf",
    "mezzanine.core",
    "mezzanine.generic",
    "mezzanine.accounts",
)

MIDDLEWARE_CLASSES = (["mezzanine.core.middleware.UpdateCacheMiddleware"] +
                      list(MIDDLEWARE_CLASSES) +
                      ["mezzanine.core.middleware.FetchFromCacheMiddleware"])
MIDDLEWARE_CLASSES.remove("mezzanine.pages.middleware.PageMiddleware")

# Mezzanine
AUTH_PROFILE_MODULE = "main.Profile"
SITE_TITLE = "Ne Istiyoruz?"
RATINGS_RANGE = (-1, 1)
RATINGS_ACCOUNT_REQUIRED = True
COMMENTS_ACCOUNT_REQUIRED = True
ACCOUNTS_PROFILE_VIEWS_ENABLED = True
ACCOUNTS_PROFILE_FORM_EXCLUDE_FIELDS = (
    "first_name",
    "last_name",
    "signup_date",
    "bio",
    "website",
    )
# Drum
ALLOWED_DUPLICATE_LINK_HOURS = 24 * 7 * 3
ITEMS_PER_PAGE = 20

try:
    from local_settings import *
except ImportError:
    pass

try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())

#DATABASES['default'] =  dj_database_url.config()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'geziparki',                      # Or path to database file if using sqlite3.
        'USER': 'geziparki',                      # Not used with sqlite3.
        'PASSWORD': '3jk9r4',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
     }
}

