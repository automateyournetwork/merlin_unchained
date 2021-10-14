from __future__ import absolute_import, unicode_literals
from celery import shared_task
import os

@shared_task(name = "Schedule All Tasks")
def run_all_tasks_job():
    os.system('pyats run job populate_db_job.py') 