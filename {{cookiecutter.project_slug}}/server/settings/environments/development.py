from server.settings.components import config

# Setting the development status:

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '0.0.0.0',
    '127.0.0.1',
    '[::1]',
] + config('DOMAIN_NAMES').split(',')
