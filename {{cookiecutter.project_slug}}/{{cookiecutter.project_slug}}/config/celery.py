from celery.schedules import crontab
from decouple import config

CELERY_BROKER_URL = ('CELERY_BROKER_URL','redis://localhost:6379/1')
CELERY_RESULT_BACKEND = ('CELERY_RESULT_BACKEND','redis://localhost:6379/0')

CELERY_BEAT_SCHEDULE = {}
