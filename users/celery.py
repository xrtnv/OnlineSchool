from celery import Celery
from celery.schedules import crontab
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DRF.settings')

app = Celery('DRF')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'deactivate-inactive-users-every-day': {
        'task': 'users.tasks.deactivate_inactive_users',
        'schedule': crontab(hour='0', minute='0'),
    },
}
