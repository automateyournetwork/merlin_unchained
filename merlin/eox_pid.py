# ----------------
# Copyright
# ----------------
# Written by John Capobianco, March 2021
# Copyright (c) 2021 John Capobianco

# ----------------
# Python
# ----------------
import os
import sys
import yaml
import time
import json
import shutil
import logging
import requests
from pyats import aetest
from pyats import topology
from pyats.log.utils import banner
from general_functionalities import ParseShowCommandFunction
from datetime import datetime
from merlin.models import EoXCredentials, EoX_PID

# ----------------
# AE Test Setup
# ----------------
class common_setup(aetest.CommonSetup):
    """Common Setup section"""
    @aetest.subsection
    def connect_to_devices(self, testbed):
        """Connect to all the devices"""
        testbed.connect(learn_hostname=True)

# ----------------
# Test Case #1
# ----------------
class Collect_Information(aetest.Testcase):
    """Parse all the commands"""

    @aetest.test
    def parse(self, testbed, section, steps):
        """ Testcase Setup section """
        # ---------------------------------------
        # Loop over devices
        # ---------------------------------------
        for device in testbed.devices.values():
            # Show Inventory to JSON
            self.parsed_show_inventory=ParseShowCommandFunction.parse_show_command(steps, device, "show inventory")
            with steps.start('Store data',continue_=True) as step:

                # Get OAuth Token
                if hasattr(self, 'parsed_show_inventory'):
                    db_key = EoXCredentials.objects.all().values('key')
                    db_user = EoXCredentials.objects.all().values('client_secret')
                    eox_pid_api_username = db_key[0]['key']
                    eox_pid_api_password = db_user[0]['client_secret']

                    oauth_token_raw = requests.post("https://cloudsso.cisco.com/as/token.oauth2?grant_type=client_credentials&client_id=%s&client_secret=%s" % (eox_pid_api_username,eox_pid_api_password))
                    oauth_token_json = oauth_token_raw.json()
                    oauth_headers = {"Authorization": "%s %s" % (oauth_token_json['token_type'],oauth_token_json['access_token'])}

                # Go Get Recommended Release using chassis PID and Oauth token
                if device.os == "nxos":
                    if "N9K-C9500v" in self.parsed_show_inventory['name']['Chassis']['pid']:
                        pid = "N9K-C93180LC-EX"
                    else:
                        pid = self.parsed_show_inventory['name']['Chassis']['pid']
                    with steps.start('Calling API',continue_=True) as step:
                        try:
                            eox_pid_raw = requests.get("https://api.cisco.com/supporttools/eox/rest/5/EOXByProductID/%s" % pid, headers=oauth_headers)
                            eox_pid_json = eox_pid_raw.json()
                        except Exception as e:
                            step.failed('Could not parse it correctly\n{e}'.format(e=e))                           
                        
                        if "EndOfSecurityVulSupportDate" in eox_pid_json:
                            security=pid['EndOfSecurityVulSupportDate']['value']
                        else:
                            security="null"

                        for pid in eox_pid_json['EOXRecord']:
                            eox_pid = EoX_PID(pyats_alias=device.alias,os=device.os,pid=pid['EOLProductID'],description=pid['ProductIDDescription'],bulletin_number=pid['ProductBulletinNumber'],bulletin_url=pid['LinkToProductBulletinURL'],external_date=pid['EOXExternalAnnouncementDate']['value'],sale_date=pid['EndOfSaleDate']['value'],sw_maintenance=pid['EndOfSWMaintenanceReleases']['value'],security=security,routine_failure=pid['EndOfRoutineFailureAnalysisDate']['value'],service_contract=pid['EndOfServiceContractRenewal']['value'],last=pid['LastDateOfSupport']['value'],svc_attach=pid['EndOfSvcAttachDate']['value'],last_updated=pid['UpdatedTimeStamp']['value'],pid_active=pid['EOXMigrationDetails']['PIDActiveFlag'],migration_information=pid['EOXMigrationDetails']['MigrationInformation'],migration_option=pid['EOXMigrationDetails']['MigrationOption'],migration_pid=pid['EOXMigrationDetails']['MigrationProductId'],migration_name=pid['EOXMigrationDetails']['MigrationProductName'],migration_strat=pid['EOXMigrationDetails']['MigrationStrategy'],migration_url=pid['EOXMigrationDetails']['MigrationProductInfoURL'],timestamp=datetime.now().replace(microsecond=0))
                            eox_pid.save()
                elif device.os == "iosxe":
                    if device.type == "Catalyst 9300":
                        for slot,value01 in self.parsed_show_inventory['slot'].items():
                            for pid,value02 in value01.items():                                                            
                                for part,value03 in value02.items():
                                    pid = value03['pid']
                                    with steps.start('Calling API',continue_=True) as step:
                                        try:
                                            eox_pid_raw = requests.get("https://api.cisco.com/supporttools/eox/rest/5/EOXByProductID/%s" % pid, headers=oauth_headers)
                                            eox_pid_json = eox_pid_raw.json()
                                        except Exception as e:
                                            step.failed('Could not parse it correctly\n{e}'.format(e=e))                           

                                        if "EndOfSecurityVulSupportDate" in eox_pid_json:
                                            security=pid['EndOfSecurityVulSupportDate']['value']
                                        else:
                                            security="null"

                                        for pid in eox_pid_json['EOXRecord']:
                                            if "EOXError" not in pid:
                                                eox_pid = EoX_PID(pyats_alias=device.alias,os=device.os,pid=pid['EOLProductID'],description=pid['ProductIDDescription'],bulletin_number=pid['ProductBulletinNumber'],bulletin_url=pid['LinkToProductBulletinURL'],external_date=pid['EOXExternalAnnouncementDate']['value'],sale_date=pid['EndOfSaleDate']['value'],sw_maintenance=pid['EndOfSWMaintenanceReleases']['value'],security=security,routine_failure=pid['EndOfRoutineFailureAnalysisDate']['value'],service_contract=pid['EndOfServiceContractRenewal']['value'],last=pid['LastDateOfSupport']['value'],svc_attach=pid['EndOfSvcAttachDate']['value'],last_updated=pid['UpdatedTimeStamp']['value'],pid_active=pid['EOXMigrationDetails']['PIDActiveFlag'],migration_information=pid['EOXMigrationDetails']['MigrationInformation'],migration_option=pid['EOXMigrationDetails']['MigrationOption'],migration_pid=pid['EOXMigrationDetails']['MigrationProductId'],migration_name=pid['EOXMigrationDetails']['MigrationProductName'],migration_strat=pid['EOXMigrationDetails']['MigrationStrategy'],migration_url=pid['EOXMigrationDetails']['MigrationProductInfoURL'],timestamp=datetime.now().replace(microsecond=0))
                                                eox_pid.save()                
