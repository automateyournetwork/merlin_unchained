from __future__ import absolute_import, unicode_literals
from celery import shared_task
import os

@shared_task(name = "run_pyATS_job")
def run_pyATS_job():
    os.system('pyats run job populate_db_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')