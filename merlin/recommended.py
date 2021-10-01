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
from merlin.models import RecommendedReleaseCredentials, RecommendedRelease

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
            self.parsed_show_inventory=ParseShowCommandFunction.parse_show_command(steps, device, "show inventory")
            self.parsed_show_version=ParseShowCommandFunction.parse_show_command(steps, device, "show version")
            with steps.start('Store data',continue_=True) as step:

                # Get OAuth Token
                if hasattr(self, 'parsed_show_inventory'):
                    db_key = RecommendedReleaseCredentials.objects.all().values('key')
                    db_user = RecommendedReleaseCredentials.objects.all().values('client_secret')
                    recommended_release_api_username = db_key[0]['key']
                    recommended_release_api_password = db_user[0]['client_secret']

                    oauth_token_raw = requests.post("https://cloudsso.cisco.com/as/token.oauth2?grant_type=client_credentials&client_id=%s&client_secret=%s" % (recommended_release_api_username,recommended_release_api_password))
                    oauth_token_json = oauth_token_raw.json()
                    oauth_headers = {"Authorization": "%s %s" % (oauth_token_json['token_type'],oauth_token_json['access_token'])}

                # Get Current Version from Device 
                if self.parsed_show_version is not None:
                    if device.os == "nxos":
                        current_version=self.parsed_show_version['platform']['software']['system_version']
                    elif device.os == "iosxe":
                        current_version=self.parsed_show_version['version']['version']

                # Go Get Recommended Release using chassis PID and Oauth token
                if "N9K-C9500v" in self.parsed_show_inventory['name']['Chassis']['pid']:
                    pid = "N9K-C93180LC-EX"
                else:
                    pid = self.parsed_show_inventory['name']['Chassis']['pid']
                with steps.start('Calling API',continue_=True) as step:
                    try:
                        recommended_release_raw = requests.get("https://api.cisco.com/software/suggestion/v2/suggestions/software/productIds/%s" % pid, headers=oauth_headers)
                    except Exception as e:
                        step.failed('Could not parse it correctly\n{e}'.format(e=e))                           
                        
                    recommended_release_json = recommended_release_raw.json()
                    for product in recommended_release_json['productList']:
                        for suggestion in product['suggestions']:
                            if 'images' in suggestion:
                                for image in suggestion['images']:
                                    if current_version == suggestion['relDispName']:
                                        compliant = "TRUE"
                                    else:
                                        compliant = "FALSE"
                                    recommended_release = RecommendedRelease(pyats_alias=device.alias,os=device.os,basePID = product['product']['basePID'],productName = product['product']['productName'],softwareType = product['product']['softwareType'],imageName = image['imageName'],description = image['description'],featureSet = image['featureSet'],imageSize = image['imageSize'],isSuggested = suggestion['isSuggested'],majorRelease = suggestion['majorRelease'],releaseTrain = suggestion['releaseTrain'],relDispName = suggestion['relDispName'],releaseDate = suggestion['releaseDate'],releaseLifeCycle = suggestion['releaseLifeCycle'],installed_version=current_version,compliant=compliant,timestamp=datetime.now().replace(microsecond=0))
                        
                                    recommended_release.save()