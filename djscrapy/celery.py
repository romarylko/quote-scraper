import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djscrapy.settings')

app = Celery('djscrapy')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.worker_max_tasks_per_child = 1

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'run_spider_at_11': {
        'task': 'quotes.tasks.parse_quotes_task',
        'schedule': crontab(hour=11, minute=0),
    },
    'run_spider_at_23': {
        'task': 'quotes.tasks.parse_quotes_task',
        'schedule': crontab(hour=23, minute=0),
    }
}
