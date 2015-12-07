# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '<EKsmvaQ|brHiO@zo#^R4@yY6'

ROOT_URLCONF = 'polls.urls'

GLOBAL_COOKIE_DOMAIN = '127.0.0.1'

INSTALLED_APPS = (
    'polls',
)

TEMPLATE_DIRS = (
    "/opt/django/polls/templates/",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)
