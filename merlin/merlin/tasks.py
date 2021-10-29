from __future__ import absolute_import, unicode_literals
from celery import shared_task
import os

@shared_task(name = "Schedule All Tasks")
def run_all_tasks_job():
    os.system('pyats run job populate_db_job.py')

@shared_task(name = "End of Life - Part ID")
def run_all_tasks_job():
    os.system('pyats run job eox_pid_job.py')

@shared_task(name = "End of Life - Serial Number")
def run_all_tasks_job():
    os.system('pyats run job eox_sn_job.py')

@shared_task(name = "End of Life - Software")
def run_all_tasks_job():
    os.system('pyats run job eox_sw_job.py')

@shared_task(name = "Learn ACL")
def run_all_tasks_job():
    os.system('pyats run job learn_acl_job.py')

@shared_task(name = "Learn ARP")
def run_all_tasks_job():
    os.system('pyats run job learn_arp_job.py')

@shared_task(name = "Learn BGP")
def run_all_tasks_job():
    os.system('pyats run job learn_bgp_job.py')

@shared_task(name = "Learn Configuration")
def run_all_tasks_job():
    os.system('pyats run job learn_config_job.py')

@shared_task(name = "Learn Interface")
def run_all_tasks_job():
    os.system('pyats run job learn_interface_job.py')

@shared_task(name = "Learn Platform")
def run_all_tasks_job():
    os.system('pyats run job learn_platform_job.py')

@shared_task(name = "Learn VLAN")
def run_all_tasks_job():
    os.system('pyats run job learn_vlan_job.py')

@shared_task(name = "Learn VRF")
def run_all_tasks_job():
    os.system('pyats run job learn_vrf_job.py')

@shared_task(name = "PSIRT")
def run_all_tasks_job():
    os.system('pyats run job psirt_job.py')

@shared_task(name = "Recommended Release")
def run_all_tasks_job():
    os.system('pyats run job recommended_job.py')

@shared_task(name = "Serial 2 Contract")
def run_all_tasks_job():
    os.system('pyats run job serial2contract_job.py')

@shared_task(name = "Show Inventory")
def run_all_tasks_job():
    os.system('pyats run job show_inventory_job.py')

@shared_task(name = "Show License Summary")
def run_all_tasks_job():
    os.system('pyats run job show_license_summary_job.py')

@shared_task(name = "Show IP Interface Brief")
def run_all_tasks_job():
    os.system('pyats run job show_ip_int_brief_job.py')

@shared_task(name = "Show Version")
def run_all_tasks_job():
    os.system('pyats run job show_version_job.py')