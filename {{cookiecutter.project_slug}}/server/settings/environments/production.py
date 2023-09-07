from server.settings.components import config

# Production flags:
# https://docs.djangoproject.com/en/4.2/howto/deployment/

DEBUG = False

ALLOWED_HOSTS = [
    # We need this value for `healthcheck` to work:
    'localhost',
] + config('DOMAIN_NAMES').split(',')  # TODO: check production hosts

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
