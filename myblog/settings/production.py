from .base import *
env = os.environ.copy()
# SECRET_KEY = env['SECRET_KEY']

DEBUG = False

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env['SECRET_KEY']


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"



try:
    from .local import *
except ImportError:
    pass
