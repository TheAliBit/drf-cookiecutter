from decouple import config

CACHE_LOCATION = config("CACHE_LOCATION", 'redis://localhost:6379/1')

CACHES = {
    'default': {
        # redis
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': CACHE_LOCATION,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

CACHE_TTL = 60 * 2
