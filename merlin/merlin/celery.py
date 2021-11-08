import os
from django.conf import settings
from celery import Celery
from celery.signals import worker_init

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_blender.settings')
app = Celery('merlin',broker='redis://redis:6379/0')

# Celery settings are in settings.py using a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(settings.INSTALLED_APPS, related_name='tasks')

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

@worker_init.connect
def init_blender(worker, **kwargs):
    if not settings.BLENDER_USE_GPU:
        get_blender()

def get_blender(filepath=settings.BLENDER_FILE, new_instance=False):
    import sys
    if 'bpy' not in sys.modules or new_instance:
        bpy = importlib.import_module('bpy')
        bpy.ops.wm.open_mainfile(filepath=filepath)
        preferences = bpy.context.user_preferences.addons['cycles'].preferences
        preferences.compute_device_type = settings.BLENDER_GPU_DEVICE if settings.BLENDER_USE_GPU else 'NONE'
        bpy.context.scene.cycles.device = 'GPU' if settings.BLENDER_USE_GPU else 'CPU'
    return sys.modules['bpy']    