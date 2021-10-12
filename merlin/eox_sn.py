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
from merlin.models import EoXCredentials, EoX_SN

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
                    eox_sn_api_username = db_key[0]['key']
                    eox_sn_api_password = db_user[0]['client_secret']

                    oauth_token_raw = requests.post("https://cloudsso.cisco.com/as/token.oauth2?grant_type=client_credentials&client_id=%s&client_secret=%s" % (eox_sn_api_username,eox_sn_api_password))
                    oauth_token_json = oauth_token_raw.json()
                    oauth_headers = {"Authorization": "%s %s" % (oauth_token_json['token_type'],oauth_token_json['access_token'])}

                # Go Get Recommended Release using chassis PID and Oauth token
                if device.os == "nxos":
                    for part,value in self.parsed_show_inventory.items():
                        for pid,value01 in value.items():
                                sn = value01['serial_number']
                                with steps.start('Calling API',continue_=True) as step:
                                    try:
                                        eox_sn_raw = requests.get("https://api.cisco.com/supporttools/eox/rest/5/EOXBySerialNumber/%s" % sn, headers=oauth_headers)
                                        eox_sn_json = eox_sn_raw.json()
                                    except Exception as e:
                                        step.failed('Could not parse it correctly\n{e}'.format(e=e))                           
                                    
                                    if "EndOfSecurityVulSupportDate" in eox_sn_json:
                                        security=pid['EndOfSecurityVulSupportDate']['value']
                                    else:
                                        security="null"
                                
                                    for pid in eox_sn_json['EOXRecord']:
                                        if "EOXError" not in pid:
                                            eox_sn = EoX_SN(pyats_alias=device.alias,os=device.os,pid=pid['EOLProductID'],description=pid['ProductIDDescription'],bulletin_number=pid['ProductBulletinNumber'],bulletin_url=pid['LinkToProductBulletinURL'],external_date=pid['EOXExternalAnnouncementDate']['value'],sale_date=pid['EndOfSaleDate']['value'],sw_maintenance=pid['EndOfSWMaintenanceReleases']['value'],security=security,routine_failure=pid['EndOfRoutineFailureAnalysisDate']['value'],service_contract=pid['EndOfServiceContractRenewal']['value'],last=pid['LastDateOfSupport']['value'],svc_attach=pid['EndOfSvcAttachDate']['value'],last_updated=pid['UpdatedTimeStamp']['value'],pid_active=pid['EOXMigrationDetails']['PIDActiveFlag'],migration_information=pid['EOXMigrationDetails']['MigrationInformation'],migration_option=pid['EOXMigrationDetails']['MigrationOption'],migration_pid=pid['EOXMigrationDetails']['MigrationProductId'],migration_name=pid['EOXMigrationDetails']['MigrationProductName'],migration_strat=pid['EOXMigrationDetails']['MigrationStrategy'],migration_url=pid['EOXMigrationDetails']['MigrationProductInfoURL'],timestamp=datetime.now().replace(microsecond=0))
                                            eox_sn.save()