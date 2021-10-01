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
from merlin.models import PSIRTCredentials, PSIRT

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
        for device in testbed:
            # Show Version to JSON
            self.parsed_show_version=ParseShowCommandFunction.parse_show_command(steps, device, "show version")
            with steps.start('Store data',continue_=True) as step:

                # Get OAuth Token
                if hasattr(self, 'parsed_show_version'):
                    db_key=PSIRTCredentials.objects.all().values('key')
                    db_user=PSIRTCredentials.objects.all().values('client_secret')
                    psirt_api_username=db_key[0]['key']
                    psirt_api_password=db_user[0]['client_secret']

                    oauth_token_raw=requests.post("https://cloudsso.cisco.com/as/token.oauth2?grant_type=client_credentials&client_id=%s&client_secret=%s" % (psirt_api_username,psirt_api_password))
                    oauth_token_json=oauth_token_raw.json()
                    oauth_headers={"Authorization": "%s %s" % (oauth_token_json['token_type'],oauth_token_json['access_token'])}

                # Get Current Version from Device 
                if self.parsed_show_version is not None:
                    if device.os == "nxos":
                        current_version=self.parsed_show_version['platform']['software']['system_version']
                    elif device.os == "iosxe":
                        current_version=self.parsed_show_version['version']['version']

                with steps.start('Calling API',continue_=True) as step:
                    try:
                        if device.os == "nxos":
                            psirt_raw=requests.get("https://api.cisco.com/security/advisories/nxos?version=%s" % current_version, headers=oauth_headers)
                        else:
                            psirt_raw=requests.get("https://api.cisco.com/security/advisories/ios?version=%s" % current_version, headers=oauth_headers)
                    
                    except Exception as e:
                        step.failed('Could not parse it correctly\n{e}'.format(e=e))                           
                        
                    psirt_json=psirt_raw.json()
                    for advisory in psirt_json['advisories']:
                        if device.os == "nxos":
                            for platform in advisory['platforms']:
                                psirt=PSIRT(pyats_alias=device.alias,os=device.os,advisory_id=advisory['advisoryId'],advisory_title=advisory['advisoryTitle'],bug_ids=advisory['bugIDs'],ips_signatures=advisory['ipsSignatures'],cves=advisory['cves'],cvrf_url=advisory['cvrfUrl'],cvss_base_score=advisory['cvssBaseScore'],cwe=advisory['cwe'],platform_name=platform['name'],ios_release=advisory['iosRelease'],first_fixed=platform['firstFixes'],first_published=advisory['firstPublished'],last_updated=advisory['lastUpdated'],status=advisory['status'],version=advisory['version'],publication_url=advisory['publicationUrl'],sir=advisory['sir'],summary=advisory['summary'],timestamp=datetime.now().replace(microsecond=0))
                        else:        
                            psirt=PSIRT(pyats_alias=device.alias,os=device.os,advisory_id=advisory['advisoryId'],advisory_title=advisory['advisoryTitle'],bug_ids=advisory['bugIDs'],ips_signatures=advisory['ipsSignatures'],cves=advisory['cves'],cvrf_url=advisory['cvrfUrl'],cvss_base_score=advisory['cvssBaseScore'],cwe=advisory['cwe'],platform_name="null",ios_release=advisory['iosRelease'],first_fixed=advisory['firstFixed'],first_published=advisory['firstPublished'],last_updated=advisory['lastUpdated'],status=advisory['status'],version=advisory['version'],publication_url=advisory['publicationUrl'],sir=advisory['sir'],summary=advisory['summary'],timestamp=datetime.now().replace(microsecond=0))
                        
                        psirt.save()