import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()


@app.task
def helloteste(self):
    print("Testando!")


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

app.conf.beat_schedule = {
    'check_address_used': {
        'task': 'registration_managament.tasks.check_address_used',
        'schedule': crontab(hour=1, minute=0),
    }
}
