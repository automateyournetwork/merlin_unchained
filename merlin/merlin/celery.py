import os
from celery import Celery

app = Celery('merlin',broker='redis://redis:6379/0')

# Celery settings are in settings.py using a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')