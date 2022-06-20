import os
import dj_database_url


SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = bool(os.environ.get('DEBUG'))
print(type(DEBUG))
print(DEBUG)

DEFAULT_CONNECTION = dj_database_url.parse(os.environ.get('HEROKU_POSTGRESQL_MAROON_URL'))
DEFAULT_CONNECTION.update({'CONN_MAX_AGE': 600})
DATABASES = {'default': DEFAULT_CONNECTION}
